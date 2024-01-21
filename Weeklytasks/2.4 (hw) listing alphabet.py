# Given a string of text, print the number of times each letter in the alphabets a-z appear. Hint: “a” != “A”. eg. Given "the quick brown fox jumps over the lazy dog", the expected output is "a: 1, b: 1, c: 1, d: 1, e: 3 ......" 

alphabets = "abdefghijklmnopqrstuvwxyz"
sentence = "the quick brown fox jumps over the lazy dog"

for i in alphabets: 
    sum = 0
    for j in sentence: 
        if i == j: 
            sum += 1
    print (str(i) +":" + str(sum))

# The str() function converts values to a string form so they can be combined with other strings.




# FAIL 
# a_count = 0 
# b_count = 0
# c_count = 0
# d_count = 0
# e_count = 0
# f_count = 0
# g_count = 0
# h_count = 0
# i_count = 0
# j_count = 0
# k_count = 0
# l_count = 0
# m_count = 0
# n_count = 0
# o_count = 0
# p_count = 0
# q_count = 0
# r_count = 0
# s_count = 0
# t_count = 0
# u_count = 0
# v_count = 0
# w_count = 0
# x_count = 0
# y_count = 0
# z_count = 0
# for i in "hello there": 
#     if i == "a""b""c""d""e""f""h""i""j""k""m""n""o""p""q""r""s""t""u""v""w""x""y""z":
#         a_count += 1
#         b_count += 1
#         c_count += 1
#         d_count += 1
#         e_count += 1
#         f_count += 1
#         g_count += 1
#         h_count += 1
#         i_count += 1
#         j_count += 1
#         k_count += 1
#         l_count += 1
#         m_count += 1
#         n_count += 1
#         o_count += 1
#         p_count += 1
#         q_count += 1
#         r_count += 1
#         s_count += 1
#         t_count += 1
#         u_count += 1
#         v_count += 1
#         w_count += 1
#         x_count += 1
#         y_count += 1
#         z_count += 1

# print(a_count,b_count,c_count,d_count,e_count,f_count,g_count,h_count,i_count,j_count,k_count,l_count,m_count,n_count,o_count,p_count,q_count,r_count,s_count,t_count,u_count,v_count,w_count,x_count,y_count,z_count)
