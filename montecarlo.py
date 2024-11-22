import numpy as np

# Probability tables
P_A = {"yes": 0.8, "no": 0.2}
P_C = {"yes": 0.5, "no": 0.5}
P_G_given_A_C = {
    ("yes", "yes"): {"Good": 0.9, "OK": 0.1},
    ("yes", "no"): {"Good": 0.7, "OK": 0.3},
    ("no", "yes"): {"Good": 0.6, "OK": 0.4},
    ("no", "no"): {"Good": 0.3, "OK": 0.7},
}
P_J_given_G = {"Good": {"yes": 0.8, "no": 0.2}, "OK": {"yes": 0.2, "no": 0.8}}
P_S_given_G = {"Good": {"yes": 0.7, "no": 0.3}, "OK": {"yes": 0.3, "no": 0.7}}

# Sampling function for each node
def sample_node(prob_table):
    return "yes" if np.random.rand() < prob_table["yes"] else "no"

def sample_G(A, C):
    prob = P_G_given_A_C[(A, C)]
    return "Good" if np.random.rand() < prob["Good"] else "OK"

# Monte Carlo Simulation
def monte_carlo_simulation(sample_size=10000):
    samples = []
    for _ in range(sample_size):
        # Sample A and C
        A = sample_node(P_A)
        C = sample_node(P_C)
        
        # Sample G based on A and C
        G = sample_G(A, C)
        
        # Sample J and S based on G
        J = sample_node(P_J_given_G[G])
        S = sample_node(P_S_given_G[G])
        
        # Store the sample
        samples.append((A, C, G, J, S))
    
    return samples

# Compute conditional probability P(S | J)
def compute_conditional_probability(samples):
    count_J_yes = 0
    count_S_yes_given_J_yes = 0
    
    for _, _, _, J, S in samples:
        if J == "yes":
            count_J_yes += 1
            if S == "yes":
                count_S_yes_given_J_yes += 1
    
    return count_S_yes_given_J_yes / count_J_yes if count_J_yes > 0 else 0

# Run simulation
sample_size = 10000
samples = monte_carlo_simulation(sample_size)
P_S_given_J = compute_conditional_probability(samples)

# Output the result
print(f"Estimated P(S | J): {P_S_given_J:.4f}")
