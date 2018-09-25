def weight_on_planets():
   weight = float(input("What do you weigh on earth? "))
   marsWeight = weight*0.38
   jupWeight = weight*2.34

   print("\nOn Mars you would weigh %.2f pounds.\nOn Jupiter you would weigh %.2f pounds." % (marsWeight, jupWeight))