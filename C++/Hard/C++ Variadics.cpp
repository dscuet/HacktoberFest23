#include <iostream>
using namespace std;

template <bool... digits>
int reversed_binary_value()
{
    int result = 0, bit_idx = 0;
    for (bool bit : {digits...})
    {
        result |= static_cast<int>(bit) << bit_idx;
        bit_idx++;
    }
    return result;
}

template <int n, bool... digits>
struct CheckValues
{
    static void check(int x, int y)
    {
        CheckValues<n - 1, 0, digits...>::check(x, y);
        CheckValues<n - 1, 1, digits...>::check(x, y);
    }
};

template <bool... digits>
struct CheckValues<0, digits...>
{
    static void check(int x, int y)
    {
        int z = reversed_binary_value<digits...>();
        std::cout << (z + 64 * y == x);
    }
};

int main()
{
    int t;
    std::cin >> t;

    for (int i = 0; i != t; ++i)
    {
        int x, y;
        cin >> x >> y;
        CheckValues<6>::check(x, y);
        cout << "\n";
    }
}
