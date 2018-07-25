import java.util.*;
public class Problem1 {


        public static void main(String[] args) {
            Scanner in=new Scanner(System.in);
            int t,l,i,c;

            t=in.nextInt();
            while(--t>=0)
            {
                c=0;
                l=in.nextInt();
                String s[]=new String[l+1];
                for(i=0;i<l;i++)
                {
                    s[i]=in.next();
                }
                s[l]=" ";

                for(i=0;i<l+1;i++)
                {
                    if(i==l)
                        break;

                    if(s[i].equals("cookie"))
                    {
                        if(!s[i+1].equals("milk"))
                        {
                            c=1;

                            break;
                        }
                        i++;
                    }
                }
                if(c==1)
                    System.out.println("NO");
                else
                    System.out.println("YES");
            }
        }

    }

