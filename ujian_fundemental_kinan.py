# no.1

# def calculate_years(principal,interest,tax,desired):
#     years = 0
#     while principal < desired :
#         principal = principal + (principal * interest) - (principal*interest*tax)
#         years += 1
#     print(years)

# calculate_years(1000.00,0.05,0.18,1100.00)
# calculate_years(1200.00,0.17,0.05,2000.00)
# calculate_years(1500.00,0.07,0.6,5000.00)

#---------------------------------------------------------------------------------------------------
# no.2

# def expandedForm(num):
#     if num > 1000 :
#         angka = (num//1000)*1000
#         sisa = num%1000
#         angka1 = (sisa//100)*100
#         sisa1 = sisa%100
#         print('{} + {} + {}'.format(angka,angka1,sisa1))
#     elif num > 10 :
#         angka = (num//10)*10
#         sisa = num%10
#         print('{} + {}'.format(angka,sisa))
# expandedForm(70304)

#---------------------------------------------------------------------------------------------
# no.3

# def tower_builder(n_floors, block_size):
#     w, h = block_size
#     z = ''
#     for item in range(n_floors):
#         z+='    '
#         for item1 in range (w-1):
#             z += '**'
#         z += '\n'
#     for item2 in range(h):
#         z +='  '
#         for item3 in range(w):
            
#             z += '***'
#         z += '\n' 
#     for item2 in range(h):
#         for item3 in range(w):
#             z += '*****'
#         z += '\n'    
#     print(z)
# tower_builder(3,(2,3))