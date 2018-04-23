
# coding: utf-8

# In[4]:


import numpy as np

from matplotlib import pyplot as plt



def v(n): #pi vector
    x=np.arange(0,n)

    x=0.5*x*np.pi/(n-1)

    return x



def integrate_cos_simple(n):

    dx=np.pi/2/n

    vector=v(n)

    tot=np.sum(np.cos(vector))

    return dx*tot



def integrate_cos_simpson(n):

    dx=np.pi/2/(n-1)*2 

    vector=np.cos(v(n))

    x_even=vector[2:-1:2] # all even

    x_odd=vector[1:-1:2] # oll odd

    tot=np.sum(x_even)/3+np.sum(x_odd)*2/3+vector[0]/6+vector[-1]/6

    return tot*dx



if __name__=='__main__':

    

    #answer to problem 2 

    print ('answering problem 2')

    t=[11,31,101,301,1001]    

    for n in t:

        bad_int=integrate_cos_simple(n)

        print ('simple integrator with ' + repr(n) + ' points has value ' + repr(bad_int))



    #answering problem 4

    print ('answering problem 4')

    points=integrate_cos_simpson(11)

    err=np.abs(points-1)

    print ('error on 11 points is ' + repr(err-1))

    for n in t:

        err=np.abs(integrate_cos_simpson(n)-1)

        print ('simpsons error on ' + repr(n) + ' is ' + repr(err))





    print ('answering problem 5')

    t=[10,30,100,300,1000]

    t=np.array(t)

    simpson_err=np.zeros(t.size)

    simple_err=np.zeros(t.size)

    for m in range(t.size):

        n=t[m]

        simpson_err[m]=np.abs(integrate_cos_simpson(n)-1)

        simple_err[m]=np.abs(integrate_cos_simple(n)-1)

    plt.plot(t,simple_err)

    plt.plot(t,simpson_err)

    ax=plt.gca()



    ax.set_yscale('log')

    ax.set_xscale('log')

    plt.show()


