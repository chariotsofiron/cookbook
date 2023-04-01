/*
Root finding algorithm.

Newton's method is a powerful technique—in general the convergence is
quadratic: as the method converges on the root, the difference between the
root and the approximation is squared (the number of accurate digits roughly
doubles) at each step. However, there are some difficulties with the method.

https://en.wikipedia.org/wiki/Newton's_method
*/
#include <cmath>       // sin, cos, fabs
#include <functional>  // std::function
#include <iomanip>     // std::setw
#include <iostream>    // std::cout
#include <optional>    // std::optional std::nullopt

double f(double x) {
    return 3 * x - cos(x) - 1;
}

double f_prime(double x) {
    return 3 + sin(x);
}

std::optional<double> newtons_method(
    std::function<double(double)> f,        // function with root to find
    std::function<double(double)> f_prime,  // derivative of the function
    double x0,                              // the initial guess
    const double tolerance,                 // precision desired
    const double epsilon  // Don't divide by number smaller than this
) {
    double x1;
    const int n = 1000;  // n iterations

    for (int i = 0; i < n; ++i) {
        double y = f(x0);
        double y_prime = f_prime(x0);

        if (y_prime < epsilon) {
            // stop if the denominator is too small
            break;
        }

        x1 = x0 - f(x0) / y_prime;  // Do Newton's computation

        if (fabs(x1 - x0) <= tolerance) {
            // Stop when the result is within the desired tolerance
            // x1 is a solution within tolerance and number of iterations
            return x1;
        }
        x0 = x1;
    }
    return std::nullopt;  // Newton's method did not converge
}

int main() {
    std::optional<double> root =
        newtons_method(f, f_prime, 1.0, 0.00001, 0.0000001);
    if (root.has_value()) {
        std::cout << "Found root:" << root.value() << std::endl;
    } else {
        std::cout << "no root found" << std::endl;
    }
}