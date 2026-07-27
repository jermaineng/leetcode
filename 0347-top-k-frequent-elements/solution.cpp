class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freqTable;

        for (int num : nums) {
            freqTable[num]++;
        }

        // organise by frequencies whereby buckets[i] stores an array of numbers that appear i times
        vector<vector<int>> buckets(nums.size() + 1);
        for (auto& [num, freq] : freqTable) {
            buckets[freq].push_back(num);
        }

        vector<int> ans;
        for (int freq = buckets.size() - 1; freq >= 1; freq--) {
            for (int num : buckets[freq]) {
                ans.push_back(num);

                if (ans.size() == k) {
                    return ans;
                }
            }
        }

        return ans;
    }
};
