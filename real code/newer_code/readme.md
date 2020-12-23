What are we expecting here?

Let us say we have a list. The list is as follows:

List = [8.1, 8.2, 24.4, 6.5, 6.6, 13]

We say there are two classes of transit here. These numbers are associated with guesses for the periods of a given exoplanet. 24.4 is approximately a multiple of 8.1 and 8.2, and so we get rid of 24.4 and say that we have found a planet that has orbital period of around 8.1 days. Likewise, we get rid fo 13, as that is approximately a multiple of 6.5 and 6.6. It is key to note that we always want to choose the smallest possible period (i.e. true period * 1).

So, how do we identify if elements in the list are multiples of other elements in the list? We have to use the modulo function. Note the following results:

8.2 mod 8.1 = 0.1
24.4 mod 8.1 = 0.1
13 mod 6.5 = 0
6.6 mod 6.5 = 0.1

Let us say we have two numbers, a and b. If a and b are multiples of one another, or if a and b are very close to one another, where a is greater than b, then a%b is always going to be close to zero, and Is probably unlikely to ever exceed 1. This can be used to identify multiples in a list. But, what happens if we do a%b where a is not close to b, or not a multiple thereof? For simplicity’s sake, we will keep a greater than b.

13 mod 8.2 = 4.8
8.1 mod 6.7 = 1.4
24.4 mod 13 = 11.4

We can see that these results are a far cry from the values less than 1 associated with multiples or duplicates. So, how do we translate this result to code?

Let us create pairs of every element in the list. These are known as tuples. We will append these tuples to a new list. As we used the assumption a > b in our calculations above, let us make sure that in every tuple, the first element is greater than the second element. Let us filter the list according to this condition.

Now, we tuple[0] mod tuple[1]. I will now go ahead and test what that gives us. 

After having run the code, I note that it is possible for the result of the modulo to be approximately equal to the b in a%b where a and b are multiples of each other. So now not only are we looking for approximately zero, we are also looking for approximately equal to other elements in the list, or really, within 5 percent of any other element in the list.

We are really dealing with parallel lists here. Let us append the modulo results to a new list. It will have the same length as the list of pairs. Now, for every element in the new list that is around zero or around some element of the list, we match it up with the smaller value in the tuple at the same index. We will take that smaller value and append it to a new, new list. Let us see what that yields, as I now go to run the code.

That has worked well, but only one problem remains. That problem is that there are duplicates (level 1) that remain in the final, reduced period list. I figure that a simple way to solve this is to compare every element in the list and see if it is within 5 percent of any other element in the list. Whether this gives us 8.1 or 8.2, for example, is irrelevant, since this period is only a guess to begin with.
