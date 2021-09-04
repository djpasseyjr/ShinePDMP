import numpy as np
from matplotlib import pyplot as plt
import event_stochastic_ode as eso

def socialf(y, t, s_slope, s_drink, gamma, a, b, m):
    """ Equations governing continuous evolution of system variables
        Returns the derivative of each entry in y at time t
    """
    s, p, d = y
    ds = s_slope*s + m(t)
    dp = gamma * (-p + eso.sigmoid(a*s) + b)
    dd = 0
    return np.array([ds, dp, dd])
    
def social_event_rule(f, y, t, dt, params):
    """ Rules governing discrete time updates to state variables. 
        To be called each timestep
    """
    s, p, d = y
    s_drink = params[1]
    if np.random.rand() < p:
            d = 1
            s -= s_drink
    else:
        d = 0
    return np.array([s, p, d])

def drinks_per_day(t, states, event_times):
    """ Compute average drinks per day given the output of the model
    and the event times.
    
    Returns
    -------
    drinks_per_day (float):
    drinks_per_encounter (float): 
    """
    event_spikes, drink_spikes = make_drink_spikes(event_times, states[:, 2], t)
    drinks_per_day = np.sum(drink_spikes) / (t[-1]-t[0])
    drinks_per_encounter = np.sum(drink_spikes) / np.sum(event_spikes)
    return drinks_per_day, drinks_per_encounter

def make_drink_spikes(event_times, drinks, t):
    """ Accept the output of a social/craving drinking model and returns
    a spike train of drinking opportunities and drinks, ready for plotting.
    
    Parameters
    ----------
    event_times (ndarray): a list of event times
    drinks (ndarray): drinking output of the model
    t (ndarray): times corresponding to the drinks array
    
    Returns
    -------
    opportunities (ndarray): zero/one array of length len(t) where ones 
        correspond to drinking opportunities
    drinkspikes   (ndarray): zero/one array of length len(t) where ones 
        correspond to drinks
    """
    opportunities = np.zeros_like(drinks)
    drinkspikes = np.zeros_like(drinks)
    dt = t[1] - t[0]
    for i, ti in enumerate(t):
        if eso.event(event_times, ti, dt):
            opportunities[i] = 1.0
            if drinks[i] == 1.0:
                drinkspikes[i] = 1.0
    return opportunities, drinkspikes

def plot_sim(
    t, 
    states, 
    event_times, 
    params, 
    figsize=[12, 6], 
    colors=["grey", "pink", "lightgreen", "orange", "darkgreen"],
    title=None
):
    s_slope, s_drink, gamma, a, b, m = params
    plt.rcParams["figure.figsize"] = figsize
    c = states[:, 0]
    p = states[:, 1]
    d = states[:, 2]
    event_spikes, drink_spikes = make_drink_spikes(event_times, d, t)
    plt.subplot(411)
    plt.plot(t, m(t), c=colors[0], alpha=0.5, label="Mood")
    plt.xticks([],[])
    plt.ylim(-1.2, 1.2)
    plt.legend()
    plt.subplot(412)
    plt.plot(t, c, c=colors[1], label="Craving")
    plt.xticks([],[])
    plt.legend()
    plt.subplot(413)
    plt.plot(t, p, c=colors[2], label="Probability of drinking")
    plt.yticks([0, .5, 1])
    plt.xticks([], [])
    plt.legend()
    plt.subplot(414)
    plt.plot(t, event_spikes, c=colors[3], label="Drinking Opportunities", alpha=0.7)
    plt.plot(t, drink_spikes, c=colors[4], label="Drinking behavior")
    plt.yticks([0, 1], ["Abstain", "Drink"])
    plt.ylim(-.2, 1.2)
    plt.xlabel("Day")
    if title is None:
        title=f"{t[-1]} Days of Drinking Behavior"
    plt.suptitle(title)
    plt.tight_layout()
    plt.legend()
    plt.show()