import numpy as np
from random import shuffle
from past.builtins import xrange

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)
  sum = 0.0
  p=0  
  
  num_train = X.shape[0]  
    
  
    
  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  
  
  for i in xrange(num_train):
    for k in range(W.shape[1]):
        if(y[i] == k):
            sum = np.sum(np.exp(X[i].dot(W)))
            p = lambda k: np.exp(X[i].dot(W)[k]) / sum
            loss += -np.log(p(y[i]))    
            dW[:, k] += -((k == y[i])-p(k)) * X[i]    
  
    
    
  loss /= X.shape[0]
  loss += 0.5 * reg * np.sum(W*W) 
  dW /= X.shape[0]  

  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)
  num_train = X.shape[0]
  #
    


  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  sum_f = np.sum(np.exp(X.dot(W)), axis=1, keepdims=True)
  p = np.exp(X.dot(W))/sum_f
  loss = np.sum(-np.log(p[np.arange(num_train), y]))
  i = np.zeros_like(p)
  i[np.arange(num_train), y] = 1
  dW = X.T.dot(p - i)
  loss /= num_train
  loss += 0.5 * reg * np.sum(W * W)
  dW /= num_train
  dW += reg*W 
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

