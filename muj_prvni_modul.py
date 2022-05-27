import datetime

nyni = datetime.datetime.now()

# Nyní máme: 10:32:04
# to-do: # Nyní máme: 27/05/2022, 10:32:04
print(f"Nyní máme: {nyni.strftime('%d/%m/%Y, %H:%M:%S')}")
