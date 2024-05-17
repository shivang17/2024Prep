# Stack is a data structure based on the theory of LIFO.

# The best example that we use in our day to day life is the browser. Each tab in a browser maintains the history of visited page. This is achieved using Stack data structure. 

# Consider browsing_session as the list of website visited in one tab

browsing_session = []
# When you visit let's say website 1 (for simplicity, we have used number, but in actual system it should be the URL of the website)
# The website will be appended to the browsing_session. 

browsing_session.append(1)
#If the user visits website 2, then we append 2.

browsing_session.append(2)
browsing_session.append(3)
print("Visited", browsing_session)
# When the user clicks on back button, simply pop the value from the list. 

# browsing_session.pop()
print("On applying back button, we removed website", browsing_session.pop())

# To check which is the current website (on top of the stack, leverage the accessing of list, index -1)
print("Current website: ", browsing_session[-1])
# When the list gets empty after removing all the website from the stack, we need to disable the button. We should leverage the falsy values in Python

if not browsing_session:
    print("Disable the back button")