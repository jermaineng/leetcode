class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        int smallerCount = 0; //count of numbers smaller than target
        int targetCount = 0; //count of numbers equal to target

        for (int num : nums) {
            if (num < target) {
                smallerCount++;
            } else if (num == target) {
                targetCount++;
            }
        }

        vector<int> ans;
        for (int i = 0; i < targetCount; i++) {
            ans.push_back(smallerCount + i);
        }

        return ans;
    }
};
