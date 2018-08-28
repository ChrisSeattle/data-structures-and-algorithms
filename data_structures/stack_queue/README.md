# stack-queue

Implementing two data structures, Stacks and Queues

## Features

Both data structures have a node.py file:
Create a Class for a Node which is aware of the value as val and next as _next
Ensure that you have a __repr__ method defined to return the value of the node when printed

In stack.py:
Create a Class for a Stack which creates an empty Stack when instantiated
This class should be aware of a default None value assigned to top when the isntance is created
This class should be aware of the len of the stack, which represents the count of Nodes in the stack at any time
This class should have the ability to accept an iterable as an argument when instantiated, such as [1, 2, 3, 4], and creates a new Node in the stack for each value in the iterable
Define any further magic methods such as len and str to support user functionality and informative responses
Define a method called push which takes any value as an argument and adds that value to the top of the stack with an O(1) Time performance
Define a method called pop which takes no arguments and removes / returns the Node at the top of the stack
Define a method called peek which takes no arguments and returns the Node at the top of the stack

In queue.py:
Create a Class for a Queue which creates an empty Queue when instantiated
This class should be aware of a default None value assigned to front when the isntance is created
This class should be aware of a default None value assigned to back when the isntance is created
This class should be aware of the len of the queue, which represents the count of Nodes in the queue at any time
This class should have the ability to accept an iterable as an argument when instantiated, such as [1, 2, 3, 4], and creates a new Node in the queue for each value in the iterable
Define any further magic methods such as len and str to support user functionality and informative responses
Define a method called enqueue which takes any value as an argument and adds that value to the back of the queue with an O(1) Time performance
Define a method called dequeue which takes no arguments and removes / returns the Node at the front of the queue

Overall:
At no time should an exception or stack trace be show to the end user. Catch and handle any such exceptions and return a printed value or operation which cleanly represents the state and either Stops execution cleanly or provides the user with clear direction and output.

## Testing

You are required to have 80% or better test coverage for each data structure.
As a general standard, you should have at least three tests for each method or body of functionality that you create in your API.
For example, you defined queue.enqueue(val)
Write a test which validates that a valid val is added to the queue when .enqueue is called
Write a test which validates that an exception is thrown if an invalid or None-type value is passed as an argument to .enqueue
Write a test which validates that the len attribute of your class increments when a new Node is added to the queue

**Author**: Chris L Chapman
