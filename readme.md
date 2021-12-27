# NongKanoon (3/12 Discord Bot)

เราสามารถใช้บอท NongKanoon เพื่อดูตารางเรียน หรือ ใช้เล่นคำสั่ง ต่างๆ ได้ (เหงา)

## Example

$classes คือ คำสั่งที่สามารถบอกตารางเรียน และเวลาได้

$clear คือ คำสั่งที่สามารถใช้เพื่อลบข้อความได้

## Optional (Class command)

1. sheet.py

เราสามารถแก้ไขการนำเข้าข้อมูลจาก `src/schedule.xlsx` ได้ เช่น keys ของ Dictionary ที่ต้องการเก็บข้อมูล หรือ วิธีในการเพิ่มข้อมูลเข้า Dictionary

```python
sheetDict = {
  "Mon": [], 
  "Tue": [], 
  "Wed": [],
  "Thu": [],
  "Fri": [],
  "Sat": [],
  "Sun": []
}
```

2. src/schedule.xlsx

เราสามารถแก้ไขรูปแบบหรือ ข้อมูลของตารางเรียนได้ เช่น การเพิ่มข้อมูลใน `cell` ต่างๆ

3. commands/class.py

เราสามารถเเก้ไขข้อมูล ข้อความที่ต้องการให้แสดงผล หรือตัวแปรที่ต้องการได้

```python
classData = sheetData(
  "src/schedule.xlsx", "B2:M6"
  # path, range
)

period =  [
  "08:10", "08:50",
  "09:30", "09:40",
  "10:20", "11:00",
  "11:40", "12:20",
  "12:30", "13:10",
  "13:50", "14:00",
  "14:40"   
  #time
]

embed = discord.Embed(
  title = f"🤔  There is no classes now",
  color = discord.Colour.gold()
)
```

ตัวอย่าง

1.classData
- ตำแหน่งของไฟล์ตารางเรียน `path` เช่น  src/schedule.xlsx
- ตำเเหน่งของ cell ที่ต้องการข้อมูล `range` เช่น B2:M6

2.period
- ช่วงเวลาของแต่ละคาบ `time` เช่น 14:40

3.embed
- ข้อความที่ต้องการแสดงไปยัง Discord `embed` => `title` เช่น 🤔  There is no classes now, `color` เช่น discord.Colour.gold()

## Credits
- Betich - [grader bot](https://github.com/betich/grader-bot)

- Chayapatr - [discord](https://github.com/chayapatr/discord)