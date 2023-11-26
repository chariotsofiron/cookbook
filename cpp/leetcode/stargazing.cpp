/*
Given a list of points, a position, and a field of view
what angle should you look to view the most points?
*/
#include <fmt/core.h>
#include <fmt/ostream.h>
#include <cmath>
#include <vector>

typedef std::pair<int32_t, int32_t> Point;

/// Field of view in radians
int solve(const std::vector<Point>& points,
          const Point start,
          const double fov) {
    // converts an (x, y)  point to an angle in degrees [0, 360)
    auto to_angle = [&start](const Point& point) {
        auto blah =
            std::atan2(point.second - start.second, point.first - start.first) *
            180 / M_PI;
        return blah < 0 ? blah + 360 : blah;
    };
    std::vector<double> angles;
    angles.reserve(points.size());
    std::transform(points.begin(), points.end(), std::back_inserter(angles),
                   to_angle);
    std::sort(angles.begin(), angles.end());

    // add 360 to the angles so we can wrap around
    std::transform(angles.begin(), angles.end(), std::back_inserter(angles),
                   [](double angle) { return angle + 360; });

    // fmt::println("Sorted points: {}", fmt::join(angles, ", "));

    // find max count of points in field of view
    int current_count = 0;
    int max_count = 0;
    size_t end_idx = 0;
    for (auto angle : angles) {
        while (end_idx < angles.size() && angles[end_idx] - angle <= fov) {
            end_idx++;
            current_count++;
        }

        if (current_count > max_count) {
            fmt::println("angle: {}, count: {}", angle + fov / 2,
                         current_count);
            max_count = current_count;
        }
        current_count--;
    }
}

int main() {
    fmt::println("Hello, world!\n");

    std::vector<Point> points{{1, 1}, {-2, 1}};
    Point start{0, 0};
    float field_of_view = 108.0f;
    solve(points, start, field_of_view);
}
