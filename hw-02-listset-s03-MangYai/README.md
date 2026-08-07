[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/vSFMUTY2)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=24293453)
# 🧠 โจทย์: หาช่วงคำที่ไม่ซ้ำกันและยาวที่สุดในรายการคำ 2 มิติ

## คำชี้แจง:
ให้เขียนฟังก์ชันที่ใช้สำหรับค้นหาช่วงของคำที่ต่อเนื่องกัน (contiguous) จากรายการคำ 2 มิติ ซึ่งเมื่อนำมารวมกันเป็นลิสต์เดียวแล้ว จะต้องหาช่วงคำที่เรียงต่อกันและไม่มีคำซ้ำ (unique words) และมีความยาวมากที่สุด  
หากมีหลายช่วงที่มีความยาวเท่ากัน ให้เก็บทุกช่วงไว้ในผลลัพธ์

---

## 🧾 ข้อกำหนดชื่อฟังก์ชัน:

```python
def longest_unique_word_sequence(words: list[list[str]]) -> tuple:
    pass
```

---

## 📥 อินพุต:

- `words` : ลิสต์ 2 มิติของคำ ซึ่งแต่ละคำเป็นสตริง ตัวอักษรภาษาอังกฤษตัวเล็กเท่านั้น (`list[list[str]]`)
- คำในแต่ละซับลิสต์มีลำดับคงที่ (เช่น เป็นประโยค หรือข้อความในลำดับเวลา)

---

## 📤 เอาต์พุต:

- ทูเพิลที่ประกอบด้วย:
  1. ความยาวของช่วงที่ไม่ซ้ำและยาวที่สุด
  2. รายการของช่วงคำเหล่านั้น (ลิสต์ของลิสต์คำ)

---

## 📌 เงื่อนไข:

- ช่วงที่พิจารณาต้องมาจากลิสต์ที่ “รวมทั้งหมดแล้วเรียงตามลำดับ” เท่านั้น
- ช่วงคำต้อง **ต่อเนื่องกัน (contiguous)** ห้ามข้าม
- คำภายในช่วงต้องไม่ซ้ำกัน
- หากมีหลายช่วงที่ยาวที่สุด ให้แสดงทั้งหมดในผลลัพธ์

---

## 🧪 ตัวอย่าง:

### ✅ ตัวอย่างที่ 1:

```python
words = [["apple", "banana"], ["apple"], ["cherry", "banana"]]
print(longest_unique_word_sequence(words))
```

**ผลลัพธ์:**

```python
(3, [
    ["banana", "apple", "cherry"],
    ["apple", "cherry", "banana"]
])
```

---

### ✅ ตัวอย่างที่ 2:

```python
words2 = [["dog", "cat"], ["mouse", "cat"], ["bird", "dog"]]
print(longest_unique_word_sequence(words2))
```

**ผลลัพธ์:**

```python
(4, [["mouse", "cat", "bird", "dog"]])
```

---

## ✅ ตรวจสอบคำตอบ (Test):

```python
python -m unittest test_list_set.py
```

