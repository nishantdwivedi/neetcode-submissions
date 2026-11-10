public class Solution {
    public bool IsAnagram(string s, string t) {
         var arr1 = new int[26];
         var arr2 = new int[26];

         if(s.Length == t.Length)
         {  
            for (int i=0; i< s.Length; i++)
            {
                 var freq1 = arr1[s[i] - 'a'];
                 arr1[s[i] - 'a'] = freq1 + 1;
                 var freq2 = arr2[t[i] - 'a'];
                 arr2[t[i] - 'a'] = freq2 + 1;
            }

            for (int i =0; i< 26; i++)
            {   
                Console.WriteLine("arr1 index:" + i + " " + arr1[i]);
                Console.WriteLine("arr2 index:" + i + " " + arr2[i]);
                if (arr1[i] != arr2[i])
                {
                    return false;
                }
            }

            return true;

         }

         return false;
    }
}
