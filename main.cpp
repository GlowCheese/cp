#ifdef ONLINE_JUDGE
#include <bits/stdc++.h>
#else
#include "debug.h"
#endif
using namespace std;

namespace {
#define fi first
#define se second
#define all(x) (x).begin(), (x).end()
using str = string;
using ll = long long;
using ld = long double;
using pll = pair<ll, ll>;
using pld = pair<ld, ld>;
using pii = pair<int, int>;

#define gint                                                                   \
  ([]() {                                                                      \
    ll x;                                                                      \
    return cin >> x, x;                                                        \
  }())
#define gstr                                                                   \
  ([]() {                                                                      \
    str x;                                                                     \
    return cin >> x, x;                                                        \
  }())
#define rpt(i, u, v) for (ll i = (u), _n_ = (v); i < _n_; i++)
#define tpr(i, u, v) for (ll i = (u), _n_ = (v); --i >= _n_;)

template <class T> using maxHeap = priority_queue<T, vector<T>>;
template <class T> using minHeap = priority_queue<T, vector<T>, greater<T>>;
template <class A, class B> bool chmax(A &a, const B b) {
  return a < b && (a = b, 1);
}
template <class A, class B> bool chmin(A &a, const B b) {
  return b < a && (a = b, 1);
}
} // namespace

const int mod = 1000000007;
const ld eps = 0.000000001, pi = acos(-1);
const ll e30 = 1ll << 30, e60 = 1ll << 60;

/* -----------------[ MAIN CODE GOES HERE ]----------------- */

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);

  
}

/* -------
    Life can't be this beautiful
        without your presence! ✨
*/
