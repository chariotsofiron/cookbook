/*
Monte Carlo a statistical method relies on repeated random sampling to obtain
numerical results. The concept is to use randomness to solve problems that
might be deterministic in principle. Monte Carlo methods are mainly used in
three problem classes: optimization, numerical integration, and generating
draws from a probability distribution.

1. Define a domain of possible inputs
2. Generate inputs randomly from a probability distribution over the domain
3. Perform a deterministic computation on the inputs
4. Aggregate the results
*/

#include <cmath>  // pow, exp, rand
#include <functional>  // std::function
#include <iostream>    // std::cout, std::endl

// Function to integrate
double func(double x) {
    return pow(x, 4) * exp(-x);
}

// Function to execute Monte Carlo integration on predefined function
double monte_carlo(std::function<double(double)> f,
                   double lower_bound,
                   double upper_bound,
                   int n) {
    double total = 0;
    for (int i = 0; i < n; i++) {
        // Select a random number within the limits of integration
        double point = lower_bound +
                       (float(rand()) / RAND_MAX) * (upper_bound - lower_bound);

        // Sample the function's values and add f(x) to the running sum
        total += f(point);
    }

    return (upper_bound - lower_bound) * total / n;
}

int main() {
    double estimate = monte_carlo(func, 1.0, 5.0, 10000000);
    std::cout << "estimate: " << estimate << std::endl;
    assert(fabs(estimate - 13.340) < 0.001);
}