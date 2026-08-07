#append = เพิ่มค่าเข้าไปใน list
fruits = ["apple", "banana", "cherry"]
more_fruits = ["manggo", "pineapple"]
for fruit in more_fruits:
    fruits.append(fruit)
print(f"fruits after append: {fruits}")

#insert = เพิ่มค่าเข้าไปใน list โดยสามารถระบุ index ได้
berries = ["raspberry", "blackberry"]
berries.insert(1, "strawberry")
berries.insert(2, "blueberry")
print(f"Berries after insert: {berries}")

#remove = ลบค่าออกจาก list
fruits_with_duplicates = ["apple", "banana", "apple", "cherry", "apple", "kiwi"]
while "apple" in fruits_with_duplicates:
    fruits_with_duplicates.remove("apple")
print(f"Fruits after removing: {fruits_with_duplicates}")

#pop = ลบและคืนค่าที่ถูกลบออกจาก list โดยสามารถระบุ index ได้


animals = ["cat", "dog", "rabbit", "hamster", "dog", "parrot",]
first_dog_index = animals.index("dog")
print(f"the first occurrence of 'dog' is at index: {first_dog_index}")

second_dog_index = animals.index("dog", first_dog_index + 1)
print(f"the second occurrence of 'dog' is at index: {second_dog_index}")

#clear = ลบทั้งหมด
#sort = เรียงน้อย > มาก
#reversed = ท้ายไปหน้า
