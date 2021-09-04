import numpy as np

def sigmoid(x):
    return 1./(1+np.exp(-x))

def f_c(t, c, m, c_slope):
    return c_slope*c - m(t)

def f_p(t, p, c, b, gamma):
    return gamma * (-p + sigmoid(p + b*c))

def event(event_times, t, dt):
    """ Return `True` if current time is an event time
    
        Parameters:
        ----------
        e (ndarray): 1d array of event times
        t (float): current time
        dt (float): timestep size
        
        Returns:
        ----------
        ev (bool): True only if any encounter time falls in the 
            interval [t, t+dt)
    """
    if type(event_times) is list:
        e = np.array(event_times)
    else:
        e = event_times
    ev = np.any((e < t + dt) * (e >= t ))
    return ev

def euler_step(f, y, t, dt, params):
    """ Returns the forward euler approximation of the change in `y` over the 
        timestep `dt`
        
        Parameters
        ----------
        f (callable): accepts `y`, `t` and all of the parameters in `params`
        y (ndarray or float): current system state
        t (float): time value
        dt (float): timestep size
        params (tuple): Tuple of parameters for `f`
        
        Returns
        -------
        dy (ndarray or float): approximation of the change in `y` 
            over the timestep `dt`
    """
    dy = f(y, t, *params) * dt
    return dy

def rk4_step(f, y, t, dt, params):
    """ Returns the fourth order runge-kutta approximation of the change in `y` over the 
        timestep `dt`
        
        Parameters
        ----------
        f (callable): accepts `y`, `t` and all of the parameters in `params`
        y (ndarray or float): current system state
        t (float): time value
        dt (float): timestep size
        params (tuple): Tuple of parameters for `f`
        
        Returns
        -------
        dy (ndarray or float): approximation of the change in `y` 
            over the timestep `dt`
    
    """
    dy1 = f(y, t, *params) * dt
    dy2 = f(y + dy1 * .5, t + dt * .5, *params) * dt
    dy3 = f(y + dy2 * .5, t + dt * .5, *params) * dt
    dy4 = f(y + dy3, t + dt, *params) * dt
    dy  = 1/6*(dy1 + dy2*2 + dy3*2 + dy4) 
    return dy


def step(t, dt, f, y, params, event_rule, event_times, method="rk4"): 
    """ Check if the current time is an encounter time, modify state 
        accordingly, then step forward one timestep
    """
    if method != "rk4" and method != "euler":
        print("Invalid method\n\"euler\" - EULER\n\"rk4\" - RK4\n")
    # If the current time is an event time
    if event(event_times, t, dt):
        y = event_rule(f, y, t, dt, params)
    # Step forward in time with desired method
    if method == "rk4": 
        dy = rk4_step(f, y, t, dt, params)  
    elif method == "euler": 
        dy = euler_step(f, y, t, dt, params)
    # Return updated states
    return y + dy, t + dt


def simulate(f, y0, start, end, dt, params, event_rule, event_times, method="rk4"):
    """ Simulate the ODE
        Parameters:
        f (callable): system derivative. Accepts `y`, `t` and all of the parameters in `params`
        y0 (ndarray or float): initial condition
        start (float): Start time
        end (float): End time
        dt (float): timestep size
        params (tuple): Tuple of parameters for `f`
        event_rule (callable): How the system responds to an event. 
            `y = event_rule(f, y, t, dt, params)` returns the updated y
            reflecting the system's response to an event.
        event_times (ndarray): 1d array of event times
        method (str): Accepts "rk4" or "euler". Default is "rk4"
    """
    assert start < end
    # Number of timesteps
    N = int((end - start) / dt)
    # Dimension of signal
    if type(y0) == float:
        n = 1
    else:
        n = len(y0)
    # Empty array for storing states
    states = np.zeros((N, n))
    # Initial conditions
    t = start
    yi = y0
    # Step forward in time and populate state array
    for i in range(N):
        yi, t = step(t, dt, f, yi, params, event_rule, event_times, method=method)
        states[i, :] = yi
    t_range = np.arange(start, end, dt)
    return states, t_range


def exponential_event_times(end_time, start_time=0.0, scale=1):
    """ Returns an array of event times where $t_{i} - t_{i-1}$ is 
    exponentially distributed.
    
    Parameters
    ----------
    end_time (float): The maximum length of time to simulate. All returned 
        event times will be strictly less than this value
    start_time (float): Initial time. Defaults to zero. All events will be 
        strictly between start_time and max_time
    scale (float): Parameter for the exponential distribution
    
    Returns
    --------
    event_times (ndarray): An array of event times with values 
        between start_time and end_time. The distance between events is
        exponentially distributed with parameter lam.
    """
    event_times = []
    current_event = start_time
    while current_event < end_time:
        next_event = current_event + np.random.exponential(scale=scale)
        event_times.append(next_event)
        current_event = next_event
    return np.array(event_times)
