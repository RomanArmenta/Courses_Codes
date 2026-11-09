import numpy as np

def markov_pi(N_trials, delta=0.3):

    N_hits = 0
    x, y = 1., 1.

    for i in range(N_trials):

        delta_x = 2 * delta * np.random.uniform() - delta
        delta_y = 2 * delta * np.random.uniform() - delta

        if np.abs(x + delta_x) < 1 and np.abs(y + delta_y) < 1:

            x += delta_x
            y += delta_y

        if x**2 + y**2 < 1:

            N_hits += 1

    return N_hits

N_trials = 4000

N_hits = markov_pi(N_trials)

print(f"Approximation of Pi using Markov sampling with {N_trials} samples: {4 * N_hits / N_trials}.")
print(f"Number of hits: {N_hits}")

# Table 1.1

N_runs = 5
cummulative_pi = 0.0
cummulative_pi_sq = 0.0
for i in range(N_runs):
    N_hits_run = markov_pi(N_trials)
    pi_value_run = 4 * N_hits_run / N_trials
    cummulative_pi += pi_value_run
    cummulative_pi_sq += pi_value_run**2
    print(f"Run: {i} | N_hits: {N_hits_run} | Estimation of pi: {pi_value_run}")

print(f"Mean value of pi: {cummulative_pi/N_runs:.5f} +- {cummulative_pi_sq/N_runs - (cummulative_pi/N_runs)**2:.5f}")