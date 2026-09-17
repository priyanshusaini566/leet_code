class Solution {
public:
    bool isPalindrome(int x) {
        int n=x;
        long int count=0;
        while(x>0){
            long int rem=x%10;
            count=count*10+rem;
            x=x/10;
        }
        if(count==n){
            return true;
        }
        else{
            return false;
        }

    }
};
int main(){
  obj=Solution();
  int a=121;
  obj.isPalindrome(a);
}
