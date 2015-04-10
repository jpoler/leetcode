//
// perms.cpp
// Author: Jon Poler
// Mail   jonathan.poler@gmail.com>
// Started on  Sun Mar 22 10:12:29 2015 Jon Poler
// Last update Mon Mar 23 19:35:52 2015 Jon Poler
//
#include <algorithm>
#include <iostream>
#include <vector>
#include <unordered_map>
#include <exception>

class bad_params_exception: public std::exception {
    virtual const char* what() const throw() {return "Invalid initial parameters";}
} bad_params_ex;
using namespace std;

class Solution {
    public:
       Solution() {}
       Solution(const Solution&) {}
       ~Solution() {}
        vector<vector<int> > permuteUnique(vector<int> &num);
        template <class T> void reverse_subseq(vector<T> &num, int i, int j);
};

vector<vector<int> > Solution::permuteUnique(vector<int> &num) {
    int k, l;
	vector<vector<int> > result;
	vector<int> new_vec(num.size());
    sort(num.begin(), num.end());
	copy(num.begin(), num.end(), new_vec.begin());
	result.push_back(new_vec);

    if (num.size() == 1) {
       return result;
    }
    while (true) {
        k = l = -1;
        int tmp;
        for (int i = num.size() - 2; i >= 0; i--) {
            if (num[i] < num[i+1]) {
                k = i;
                break;
            }
        }
        if (k == -1) {
           break;
        }
        for (int i = num.size() - 1; i > k; i--) {
            if (num[i] > num[k]) {
                l = i;
            }
        }
        tmp = num[k];
        num[k] = num[l];
        num[l] = tmp;
        cout << "before reverse: ";
        for (vector<int>::const_iterator it = num.begin(); it != num.end(); it++) {
            cout << *it << " ";
        }
        cout << endl;
        cout << "from indicies (k, l): " << k << " " << l << endl;
        this->reverse_subseq<int>(num, k+1, num.size() - 1);
        cout << "after reverse: ";
        for (vector<int>::const_iterator it = num.begin(); it != num.end(); it++) {
            cout << *it << " ";
        }
        cout << endl;

        vector<int> new_vec(num.size());
        std::copy(num.begin(), num.end(), new_vec.begin());
        result.push_back(new_vec);
    }
    return result;
}

template <class T> void Solution::reverse_subseq(vector<T> &num, int i, int j) {
    T tmp;
    while (i < j) {
        tmp = num[i];
        num[i] = num[j];
        num[j] = tmp;
        i++; j--;
    }
}


int main() {
    vector<vector<int> > permutations;
    Solution s;
    int inp_arr[] = {1,2,3, 4};
    std::vector<int> inputs(inp_arr, inp_arr + sizeof(inp_arr) / sizeof(int));
    permutations = s.permuteUnique(inputs);
    cout << "permuatations.size(): " << permutations.size() << endl;
    for (vector<vector<int> >::const_iterator it1 = permutations.begin(); it1 != permutations.end(); it1++) {
        for (vector<int>::const_iterator it2 = (*it1).begin(); it2 != (*it1).end(); it2++) {
        	cout << *it2 << " ";
        }
    	cout << endl;
    }
	return 0;
}
