import streamlit as st
import Milk as M
from PIL import Image

with st.sidebar:
    st.title('ᗰIᒪK🐮🥛')
    menu = st.selectbox('menu', ('Prediction Milk Quality⤵️', 'Quality of Milk➡️', 'Type of Milk➡️', 'Benefits & blame of Milk➡️'))

#หน้า 1
if menu == 'Prediction Milk Quality⤵️':
    M.Milkk()
if menu == 'Quality of Milk➡️': #หน้า 2
    # st.markdown(
    #     f"""
    #     <style>
    #     .stApp {{
    #     background-image: url("https://www.grahamowengallery.com/fishing/New_Zealand_2012/deck-view-2.jpg");
    #     background-attachment: fixed;
    #     background-size: cover;
    #     /* opacity: 0.3; */
    #     }}
    #     </style>
    #     """,
    #     unsafe_allow_html=True
    # )
    st.title('✦Quaility of Milk🍼')
    cow = Image.open('cow.jpg')
    st.image(cow)
    st.caption('''น้ำนมดิบ raw milk เป็นวัตถุดิบหลักเพื่อการแปรรูปเป็นผลิตภัณฑ์นมหลายชนิด เช่น น้ำนมพาสเจอไรซ์ นมเปรี้ยว โยเกิร์ต นมผง เนยแข็ง คุณภาพน้ำนมดิบ
มีผลโดยตรงต่อคุณภาพของผลิตภัณฑ์''')
    st.info('𖧷˚ ༘ คุณภาพทางกายภาพและเคมี🧪')
    st.info('𖧷˚ ༘คุณภาพด้านจุลินทรีย์🦠')
    st.info('𖧷˚ ༘คุณภาพของน้ำนมดิบตามมาตรฐาน มกอช🥛✦')

    st.subheader('𝐩𝐡𝐲𝐬𝐢𝐜𝐚𝐥 𝐚𝐧𝐝 𝐜𝐡𝐞𝐦𝐢𝐜𝐚𝐥 𝐦𝐢𝐥𝐤 𝐪𝐮𝐚𝐥𝐢𝐭𝐲')
    st.caption('''🍒1. สี ปกติ สีของน้ำนม มีสีขาวหรือสีขาวนวล

🍒2. pH น้ำนมวัวในธรรมชาติเป็นกรดเล็กน้อยหรือที่ระดับค่อนข้างเป็นกลาง คือที่ pH 6.6-6.8 เนื่องจากองค์ประกอบ เช่น เคซีน (casein), albumin, globulin,
citrate, phosphate และ CO2 รวมทั้งเกลือแร่ต่างๆ ที่ละลายอยู่ ความเป็นกรดดังกล่าว คือความเป็นกรดตามธรรมชาติ น้ำนมจากโคนมที่เป็นโรคเต้านมอักเสบ
จะมีฤทธิ์เป็นด่าง การวัดค่าความเป็นกรด-ด่าง ทำได้โดยใช้เครื่อง pH meter

🍒3. ส่วนประกอบ ส่วนประกอบส่วนใหญ่ของน้ำนมคือ น้ำซึ่งมีอยู่ประมาณ 87% ส่วนที่เหลือคือไขมันนม และของแข็งในน้ำนมที่ไม่รวมไขมัน (milk solid not fat)
ซึ่งประกอบด้วย โปรตีน น้ำตาลแล็กโทส เกลือแร่ วิตามิน ซึ่งเกณฑ์ที่ใช้ในการให้ราคาน้ำนมดิบ ในประเทศไทย คือเปอร์เซ็นต์ไขมันนม และเปอร์เซ็นต์ของแข็ง
ในน้ำนมท่ีไม่รวมไขมัน (milk solid not fat) ส่วนประกอบต่างๆ ในน้ำนม จะมีค่าสูงหรือต่ำขึ้นอยู่กับอาหารที่เลี้ยงโคนม พันธุ์โคนม ฤดูกาล ระยะเวลาให้น้ำนม
อายุของโคนม สุขภาพของโค คุณลักษณะเฉพาะตัวของโคนม และวิธีการรีดน้ำนม
การตรวจวิเคราะห์ส่วนประกอบน้ำนมอาจใช้เครื่องมืออัตโนมัติ

ซึ่งสามารถตรวจหาค่าส่วนประกอบต่างๆ ได้ทั้ง ไขมัน โปรตีน น้ำตาลแล็กโทส ของแข็งในน้ำนมที่ไม่รวมไขมันและของแข็งทั้งหมดในน้ำนมในเวลาเดียวกัน

มกอช. ได้กำหนดให้น้ำนมดิบคุณภาพดีควรมีส่วนประกอบน้ำนม ดังนี้

ไขมันนม (butter fat) โดยทั่วไปไขมันนมมีค่าอยู่ระหว่าง 3.2-3.5 น้ำนมดิบตามมาตรฐาน มกอช กำหนดให้มีปริมาณไขมันนมไม่น้อยกว่าร้อยละ 3.2

โปรตีน (protein) ไม่น้อยกว่าร้อยละ 2.8 ของแข็งทั้งหมดในน้ำนมไม่รวมไขมัน  ไม่น้อยกว่าร้อยละ 8.25 ของแข็งทั้งหมดไม่น้อยกว่าร้อยละ 12
การตรวจนับจำนวนเซลล์เม็ดเลือดขาวในน้ำนมดิบ (somatic cell count) ไม่มากกว่า 500,000 เซลล์/มิลลิลิตร

🍒4. จุดเยือกแข็ง (freezing point) เพื่อตรวจการปลอมปนน้ำ โดยใช้เครื่องหาจุดเยือกแข็ง (Cryoscope) น้ำนมดิบคุณภาพดีควรมีค่าจุดเยือกแข็งระหว่าง
-0.520 ถึง -0.525 องศาเซลเซียส

🍒5. ค่าความถ่วงจำเพาะ (specific gravity) ใช้เครื่องมือแล็กโทมิเตอร์ (Lactometer) ซึ่งปกติความถ่วงจำเพาะของน้ำนมอยู่ระหว่าง 1.028 ถึง 1.034 g/ml
ที่อุณหภูมิ 20 องศาเซลเซียส น้ำนมดิบตามมาตรฐานมีค่าความถ่างจำเพาะไม่ต่ำกว่า 1.028''')
    cow = Image.open('milk composition.bmp')
    st.image(cow)
    st.subheader('𝐦𝐢𝐜𝐫𝐨𝐛𝐢𝐚𝐥 𝐪𝐮𝐚𝐥𝐢𝐭𝐲')
    st.caption('''🚪คุณภาพด้านจุลินทรีย์ ━━━━━★

🦠1. การประมาณจำนวนจุลินทรีย์ โดยดูการเปลี่ยนสีของน้ำยาหรือการทดสอบรีดักชัน จะสามารถแบ่งเกรดของน้ำนมได้ เพราะปริมาณจุลินทรีย์ที่มีอยู่ในน้ำนม
จะทำให้สีของน้ำยาทดสอบเปลี่ยนแปลงไปตามระยะเวลาหลังจากที่เติมน้ำยานั้นลงไปในตัวอย่างน้ำนม

การตรวจสอบแบ่งเป็น 2 ชนิด ตามชนิดของน้ำยาที่ใช้ คือเมทิลีนบลูและรีซาซูรีิน

การทดสอบเมทิลีนบลูรีดักชัน ดูการเปลี่ยนแปลงของสีหลังจากเติมน้ำยาเมทิลีนบลู และบ่มที่อุณหภูมิ 37 องศาเซลเซียส การอ่านผลให้อ่านผลครั้งแรก
หลังจากเติมน้ำยาไปแล้วครึ่งชั่วโมงและอ่านผลหลังจากนั้นทุกๆ ชั่วโมง จนถึง 6 ชั่วโมง ตัวอย่างที่มีจุลินทรีย์มากจะเปลี่ยนสีของน้ำยาจากสีฟ้าอมเขียว
เป็นสีขาว

การทดสอบรีซาซูรีนรีดักชัน ดูการเปลี่ยนแปลงสีหลังจากเติมน้ำยารีซาซูรินและบ่มที่อุณหภูมิ 37 องศาเซลเซียส การอ่านผลให้อ่านหลังจากเติมน้ำยา 1 ชั่วโมง
หรืออ่านผลในชั่วโมงที่ 1 และ 3 การเปลี่ยนสีของน้ำยารีซาซูริน จะเปลี่ยนจากสีม่วงน้ำเงินเป็นสีม่วงแดง ชมพู หรือขาว ตามจำนวนจุลินทรีย์ที่มีอยู่ในน้ำนมนั้น

🦠2. การตรวจนับปริมาณจุลินทรีย์

จุลินทรีย์ในน้ำนมที่ตรวจเป็นงานประจำ ได้แก่ แบคทีเรีย ยีสต์ และรา จำนวนจุลินทรีย์ในน้ำนมจะมีปริมาณมากหรือน้อย ขึ้นอยู่กับขั้นตอนต่างๆ ตั้งแต่การปฏิบัติ
ต่อโคนมในขณะรีดนม การทำความสะอาด การจัดการสุขาภิบาลในคอก และการปนเปื้อนจากภาชนะที่ใช้ในการรีดนมหรือผู้รีดนม

 

การตรวจทางจุลชีววิทยา สามารถแบ่งเป็นการตรวจนับจำนวนจุลินทรีย์ทั้งหมด การตรวจหาแบคทีเรียกลุ่มโคลิฟอร์มการตรวจนับแบคทีเรียที่ทนความร้อน
(thermophilic bacteria) การตรวจนับแบคทีเรียที่ชอบความเย็นวิธีในการตรวจนับทางจุลชีววิทยา จะทำโดยใช้อาหารเลี้ยงเชื้อ (nutrient agar) ผสมกับน้ำนม
หรือน้ำนมที่เจือจางแล้วให้เข้ากันในจานอาหารเลี้ยงเชื้อ จากนั้นจะเพาะจานอาหารเลี้ยงเชื้อไว้ โดยบ่มที่อุณหภูมิระดับต่างๆ ตามแต่ชนิดของการตรวจสอบ

🥤1. การตรวจนับจุลินทรีย์ทั้งหมด (standard plate count) น้ำนมที่สะอาดคุณภาพยอดเยี่ยมจะมีจุลินทรีย์เพียง 1,000 เซลล์ต่อน้ำนม 1 มิลลิลิตร

ในประเทศไทยให้คุณภาพน้ำนมเกรดหนึ่งมีจำนวน 100,000 เซลล์ต่อน้ำนม 1 มิลลิลิตร จุลินทรีย์ในน้ำนมสามารถตรวจนับได้หลังจากบ่มที่อุณหภูมิ 32 องศาเซลเซียส
เป็นเวลา 48 ชั่วโมง

มาตรฐานผลิตภัณฑ์อุตสาหกรรม (มอก.) ได้กำหนดให้น้ำนมดิบที่นำมาผลิตเป็นน้ำนมสดมีจุลินทรีย์ทั้งหมดในน้ำนมไม่เกิน 400,000 เซลล์ต่อน้ำนม 1 มิลลิลิตร

 

🥤️2. การตรวจหาแบคทีเรียกลุ่มโคลิฟอร์ม (coliform) แบคทีเรียในกลุ่มโคลิฟอร์ม พบได้ในลำไส้ของคนและสัตว์ ในอุจจาระ ในโคนมที่เป็นโรคเต้านมอักเสบ
ในภาชนะรีดนม หรือในคอกซึ่งล้างทำความสะอาดไม่ทั่วถึง หากตรวจพบจุลินทรีย์กลุ่มนี้มากกว่า 100 เซลล์ต่อน้ำนม 1 มิลลิลิตร การปนเปื้อนของแบคทีเรียกลุ่มนี้
แสดงถึงสุขลักษณะที่ไม่ดีของการรีดนม วิธีการตรวจสอบแบคทีเรียในกลุ่มโคลิฟอร์ม ทำโดยใช้อาหารเลี้ยงเชื้อสำหรับหาจุลินทรีย์กลุ่มนี้ผสมกับน้ำนม แล้วบ่มที่อุณหภูมิ
37 องศาเซลเซียส เป็นเวลา 24 ชั่วโมง หลังจากนั้นตรวจนับจำนวนจุลินทรีย์ที่มีลักษณะเฉพาะที่ขึ้นในจานอาหารเลี้ยงเชื้อนั้น
 

🥤3. การตรวจนับแบคทีเรียที่ทนความร้อน (thermophilic bacteria) แบคทีเรียสามารถแบ่งเป็นชนิดตามอุณหภูมิที่เจริญในน้ำนม จะมีแบคทีเรียที่สามารถมีชีวิตอยู่ได้
ภายหลังกระบวนการพาสเจอไรซ์ซึ่งแบคทีเรียนี้จะอยู่ตามเต้านมและภาชนะใส่นม ในน้ำนมที่มีจำนวนแบคทีเรียทั้งหมดมาก มีแบคทีเรียชนิดนี้อยู่มากและมีผลทำให้อายุการ
เก็บรักษาน้ำนมนั้นสั้นลง
 

การตรวจแบคทีเรียในกลุ่มนี้จะต้องทำน้ำนมให้ร้อนเสียก่อนที่อุณหภูมิ 62 องศาเซลเซียส เป็นเวลา 30 นาที จากนั้นนำตัวอย่างน้ำนมนั้น มาตรวจโดยใช้วิธีเดียว
กับการตรวจนับจำนวนแบคทีเรียทั้งหมด
 

ประกาศกระทรวงสาธารณสุข ระบุให้น้ำนมพาสเจอไรซ์มีแบคทีเรียได้ไม่เกิน 10,000 เซลล์ ต่อน้ำนม 1 มิลลิลิตร
 

การตรวจนับแบคทีเรียที่ชอบความเย็น ยังมีแบคทีเรียอีกกลุ่มหนึ่งในน้ำนมซึ่งเจริญได้ดีที่อุณหภูมิต่ำ แบคทีเรียกลุ่มนี้พบได้ในเต้านมและในถังนม ซึ่งมีอุณหภูมิที่ลดต่ำ
2-7 องศาศาเซลเซียส ส่วนใหญ่ของจุลินทรีย์กลุ่มนี้สามารถถูกทำลายได้ด้วยความร้อน หากยังมีอยู่ในน้ำนมจะทำให้คุณภาพของน้ำนมนั้นลดลง มักทำให้เกิดกลิ่นอัน
ไม่พึงประสงค์ เพราะจุลินทรีย์พวกนี้จะสร้างน้ำย่อยออกมาย่อยโปรตีนและไขมันในน้ำนม ทำให้น้ำนมเสื่อมคุณภาพและเน่าเสียได้
 ''')

    st.subheader('𝐍𝐚𝐭𝐢𝐨𝐧𝐚𝐥 𝐁𝐮𝐫𝐞𝐚𝐮 𝐨𝐟 𝐀𝐠𝐫𝐢𝐜𝐮𝐥𝐭𝐮𝐫𝐚𝐥 𝐂𝐨𝐦𝐦𝐨𝐝𝐢𝐭𝐲 𝐚𝐧𝐝 𝐅𝐨𝐨𝐝 𝐒𝐭𝐚𝐧𝐝𝐚𝐫𝐝𝐬. ')
    st.write('ᯅ━━━━━★━━━━━★━━━━━★━━━━━★━━━━━★━━━━━★━━━━━★ᯅ')
    st.title('cℓιcк мє👇')
    st.write("[🖇️ข้อมูลเพิ่มเติม](https://www.dpo.go.th/%E0%B8%A1%E0%B8%B2%E0%B8%95%E0%B8%A3%E0%B8%90%E0%B8%B2%E0%B8%99%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%8B%E0%B8%B7%E0%B9%89%E0%B8%AD%E0%B8%99%E0%B9%89%E0%B8%B3%E0%B8%99%E0%B8%A1/)")

if menu == 'Type of Milk➡️':

    st.title('🥛รู้จักประเภทนมพร้อมดื่ม นมแบบไหนมีประโยชน์ยังไงบ้าง🛒')
    cow = Image.open('type1.jpg')
    st.image(cow)
    st.subheader('✦ นมสด (𝐖𝐡𝐨𝐥𝐞 𝐌𝐢𝐥𝐤)')
    cow = Image.open('drink.jpg')
    st.image(cow)
    st.caption(''' นมที่นำมาบรรจุกล่องหรือขวดขายกันอยู่ตามท้องตลาดนั้นจะเป็นนมที่ผ่านกระบวนการต่าง ๆ อย่างการฆ่าเชื่อหรือนำส่วนผสมบางอย่างออกไป แต่สำหรับนมสดนั้นจะเป็นน้ำนมที่รีดออกมาสดใหม่โดยยังไม่ผ่านกระบวนการต่าง ๆ นั่นเองค่ะ สารอาหารในน้ำนมจะครบถ้วนสมบูรณ์ แถมกลิ่นและรสชาติก็ยังหอมมันที่สุด เพียงแค่นมสดนั้นจะไม่สามารถเก็บไว้ได้นานเพราะมีจุลินทรีย์ที่ทำให้นมเสียได้เร็ว จึงต้องมีการนำไปฆ่าเชื้อด้วยกระบวนการต่าง ๆ ก่อนค่ะ''')

    st.subheader('✦ นมพาสเจอร์ไรส์ (𝐏𝐚𝐬𝐭𝐞𝐮𝐫𝐢𝐳𝐞𝐝  𝐌𝐢𝐥𝐤)')
    cow = Image.open('pass.jpg')
    st.image(cow)
    st.caption(''' นมพาสเจอร์ไรส์เป็นนมที่ผ่านกระบวนการฆ่าเชื้อจุลินทรีย์ที่หมดอายุเร็วที่สุด แต่ก็มีคุณค่าทางอาหารและรสชาติหอมมันใกล้เคียงกับนมสดมากที่สุดเช่นกัน โดยมีการฆ่าเชื้อทั้งแบบที่ใช้เวลาสั้นและนานตั้งแต่ 15 วินาที ไปจนถึง 30 นาทีเลยค่ะ อุณหภูมิที่ใช้จะอยู่ที่ 63 – 72 องศาเซลเซียส การฆ่าเชื้อนี้จะทำลายจุลินทรีย์บางส่วนที่ส่งผลเสียต่อร่างกาย แต่ไม่ได้ทำลายตัวที่ทำให้นมเน่าเสียได้ เพราะอย่างนี้นมพาสเจอร์ไรส์จึงต้องแช่เย็นที่อุณหภูมิต่ำกว่า 10 องศาตลอดเวลา แถมอยู่ได้เต็มที่แค่ 7 -10 วันเท่านั้นเองด้วย ถ้าหากเดินผ่านตู้แช่เย็นในห้างและเห็นนมที่บรรจุใส่ขวดพลาสติกขุ่นหรือกล่องเอาไว้ ส่วนใหญ่ก็จะเป็นนมพาสเจอร์ไรส์ทั้งหมดเลย''')

    st.subheader(' ✦ นมสเตอริไลส์ (𝐒𝐭𝐞𝐫𝐢𝐥𝐢𝐳𝐞𝐝  𝐌𝐢𝐥𝐤)')
    cow = Image.open('ster.jpg')
    st.image(cow)
    st.caption('''นมที่ผ่านกระบวรการฆ่าเชื้อจุลินทรีย์รูปแบบต่อมาคือนมสเตอริไลส์ค่ะ ซึ่งก็จะมีการใช้เวลาและอุณหภูมิมากขึ้นอีกหน่อย โดยจะอยู่ที่ 100 -135 องศาเซลเซียส เป็นเวลา 20-30 นาที ทำให้จุลินทรีย์ทั้งชนิดที่ส่งผลเสียต่อร่างกายและทำให้อาหารเน่าเสียถูกทำลายจนหมด นมที่ได้ก็จะเก็บไว้โดยไม่ต้องแช่เย็นได้ถึง 1 ปี และมักจะบรรจุในกระป๋องอลูมิเนียมที่ปิดสนิท แม้นมสเตอริไรส์นั้นจะเป็นน้ำนมที่ได้คุณภาพแต่ก็สูญเสียวิตามินบางชนิดไป ทำให้ไม่เหมาะสำหรับเด็ก ๆ ที่อยู่ในวัยกำลังโต เพราะอาจได้สารอาหารไม่ครบ และการใช้ความร้อนที่สูงทำให้รสชาติของนมสเตอริไรส์ยังเปลี่ยนไปค่อนข้างเยอะ ความหอมอร่อยจึงอาจสู้นมประเภทอื่น ๆ ไม่ได้''')

    st.subheader('✦ นมยูเอชที (𝐔𝐇𝐓, 𝐔𝐭𝐫𝐚 𝐇𝐢𝐠𝐡 𝐓𝐞𝐦𝐩𝐞𝐫𝐚𝐭𝐮𝐫𝐞 𝐌𝐢𝐥𝐤)')
    cow = Image.open('uht.jpg')
    st.image(cow)
    st.caption('''มาถึงนมที่ผ่านกระบวนการฆ่าเชื่อด้วยความร้อนรูปแบบสุดท้ายหรือนมยูเอชที (UHT) ที่ย่อมาจาก Ultra-High-Temperature Short Time  หมายถึงการใช้ความร้อนที่สูงมากในระยะเวลาสั้น ๆ โดยเป็นการใช้อุณหภูมิที่สูงถึง 135-150 เพียง 2-4 วินาทีเท่านั้น เป็นกระบวนการที่กำจัดเชื้อจุลินทรีย์ออกไปได้เกือบทั้งหมดแต่ก็แทบไม่ได้เสียวิตามินออกไปเลย แถมรสชาติก็และความอร่อยก็ยังแทบไม่เปลี่ยน ถึงอย่างนั้น นมยูเอชทีก็ยังมีทั้งแบบที่ผลิตจากนมผงและนมสดโดยตรง โดยทั้งหมดมักจะอยู่ในรูปแบบกล่องกระดาษขนาดกะทัดรัดพร้อมหลอดให้เจาะดื่มได้สะดวก ซึ่งจะเก็บได้โดยไม่ต้องแช่เย็นนาน 6-8 เดือน เป็นนมที่ดื่มง่าย เหมาะกับสมาชิกทุกคนบ้านยกเว้นเด็กทารกที่อายุต่ำกว่า 1 ปี''')

    st.subheader('✦ นมไขมันต่ำหรือนมพร่องมันเนย (𝐋𝐨𝐰 𝐅𝐚𝐭 𝐌𝐢𝐥𝐤)')
    cow = Image.open('fat.jpg')
    st.image(cow)
    st.caption(''' ไม่ว่าจะเป็นนมพร่องมันเนย นมไขมันต่ำ หรือนม Low fat ก็คือนมประเภทเดียวกันทั้งหมดค่ะ ซึ่งนมประเภทนี้จะถูกสกัดไขมันออกไปให้เหลือไม่เกิน 15% แต่สารอาหารชนิดอื่น ๆ ก็ยังคงอยู่นะคะ นี่จึงเป็นนมที่เหมาะกับผู้สูงอายุและผู้ป่วยที่มีปัญหาไขมันในเส้นเลือดสูง รวมทั้งผู้ที่อยากควบคลุมพลังงานในแต่ละวันด้วย แต่จะไม่เหมาะสำหรับเด็กในวัยกำลังโตที่ต้องการพลังงานและสาอาหารอย่างครบถ้วน ซึ่งนมประเภทนี้ก็สามารถเป็นได้ทั้งนมในรูปแบบพาสเจอร์ไรส์ สเตอริไลส์และยูเอชที''')

    st.subheader('✦ นมขาดมันเนย (𝐒𝐤𝐢𝐦 𝐌𝐢𝐥𝐤 ,𝐍𝐨𝐧-𝐅𝐚𝐭 𝐌𝐢𝐥𝐤)')
    cow = Image.open('nonfat.jpg')
    st.image(cow)
    st.caption(''' นมขาดมันเนยหรือนม Non-Fat จะเป็นนมที่ถูกสกัดไขมันออกไปจนเกือบหมดเหลือเพียง 0.15% เท่านั้น ส่วนสารอาหารที่ยังคงอยู่ก็จะเป็นพวกโปรตีนและคาร์โบไฮเดรต แต่วิตามินที่ละลายในไขมันก็อาจเหลืออยู่ไม่มากค่ะ นมขาดมันเนยจึงเหมาะกับผู้ที่ร่างกายมีปัญหาเรื่องไขมันจริง ๆ เท่านั้น ถ้าสำหรับเด็ก ๆ และผู้ที่ร่างกายแข็งแรงปกติ การดื่มนมประเภทอื่นจะทำให้ร่างกายได้คุณประโยชน์และสารอาหารที่จำเป็นมากกว่า เพราะไขมันจากนมนั้นเป็นไขมันที่ให้ประโยชน์และยังอยู่ในปริมาณที่พอดีกับความจำเป็นของร่างกายในแต่ละวันด้วย''')

    st.subheader('✦ นมเปรี้ยว (𝐅𝐞𝐫𝐦𝐞𝐧𝐭𝐞𝐝 𝐌𝐢𝐥𝐤)')
    cow = Image.open('som.jpg')
    st.image(cow)
    st.caption(''' นมเปรี้ยวเป็นนมที่มีรสชาติต่างจากนมประเภทอื่นมากที่สุดเลยค่ะ นั่นเป็นเพราะกระบวนการเติมแบคทีเรียที่ช่วยให้กระเพาะอาหารและลำไส้ทำงานได้เป็นปกติ จากนั้นก็ได้มีการนำไปหมักต่อเพื่อเพิ่มเชื้อจุลินทรีย์ที่เป็นประโยชน์ นมสดธรรมดาจึงกลายมาเป็นนมที่มีรสเปรี้ยวอย่างที่เห็น น้ำตาลในนมก็จะถูกเปลี่ยนให้กลายเป็นกรด นมเปรี้ยวจึงเป็นนมอีกประเภทที่ตอบโจทย์สำหรับคนที่มีปัญหาเรื่องการย่อยน้ำตาลในนม''')

    st.subheader('✦ นมผง (𝐃𝐫𝐢𝐞𝐝 𝐌𝐢𝐥𝐤 ,𝐏𝐨𝐰𝐝𝐞𝐫 𝐌𝐢𝐥𝐤)')
    cow = Image.open('nompong.jpg')
    st.image(cow)
    st.caption('''หลายคนอาจกังวลว่านมผงนั้นจะได้คุณประโยชน์ไม่เท่านมสด แต่จริง ๆ แล้วนมผงนั้นก็คือการนำนมสดมาระเหยน้ำออกไปจนหมดเท่านั้นเองค่ะ ส่วนสารอาหารต่าง ๆ ก็ถือว่าแทบไม่ได้สูญเสียไปเลย มีเพียงวิตามินบางตัวเท่านั้นที่อาจหายไป กลิ่นและรสชาติของนมก็เปลี่ยนไปเพียงนิดเดียว ซึ่งข้อดีของนมผงคือการเก็บรักษาที่ง่ายและมีอายุยาวนาน โดยนมผงนั้นอยู่ได้นานถึง 1 ปีครึ่งเลยค่ะ ถ้าหากเปิดแล้วเก็บไว้ในซองปิดสนิทโดยไม่เจอความชื้น แต่ถ้าหากมีการเปิดและเทแบ่งใส่ภาชนะอื่นก็จะอยู่ได้นาน 3 เดือน ส่วนนมผงที่นำไปผสมน้ำชงเรียบร้อยแล้วก็ควรดื่มภายใน 1 ชั่วโมง เพื่อให้ได้รับคุณค่าทางอาหารมากที่สุด แต่ถ้าหากมีความจำเป็นก็สามารถแช่เย็นเอาไว้ได้ 24 ชั่วโมง''')
if menu == 'Benefits & blame of Milk➡️': #หน้า 4
    st.title('🔖รวม 8 ประเภทของนม นมแบบไหนเหมาะกับคุณรวม 8 ประเภทของนม นมแบบไหนเหมาะกับคุณ₍ᐢ..ᐢ₎')

    st.subheader('นมวัว🐄')
    st.subheader('𝗯𝗲𝗻𝗲𝗳𝗶𝘁👍')

    st.caption('''★ วิตามินบี 12 สูง มีส่วนช่วยการทำงานของระบบประสาทและสมอง

★ วิตามินบี 2 สูง ช่วยให้ร่างกายได้พลังงานจากคาร์โบไฮเดรตโปรตีนและไขมัน

★ แคลเซียมสูง มีส่วนช่วยในกระบวนการสร้างกระดูกและฟันที่แข็งแรง

★ ฟอสฟอรัสสูง มีส่วนช่วยในกระบวนการสร้างกระดูกและฟันที่แข็งแรง

★ ไอโอดีนสูง''')

    st.subheader('𝗯𝗹𝗮𝗺𝗲👎')
    cow = Image.open('tost.jpg')
    st.image(cow)

    st.subheader('นมแพะ🐐')
    st.subheader('𝗯𝗲𝗻𝗲𝗳𝗶𝘁👍')
    st.caption('''📌 ดีต่อระบบย่อยอาหาร
★ ส่งเสริมระบบภูมิคุ้มกัน

★ ลดระดับคอเลสเตอรอล

★ เสริมสร้างพัฒนาการของทารก 

★ ช่วยลำเลียงวิตามินต่าง ๆ ที่เป็นประโยชน์ต่อร่างกาย 

★ ช่วยปกป้องและรักษาโรคได้''')
    st.subheader('𝗯𝗹𝗮𝗺𝗲👎')
    st.caption('''🎈 ในนมแพะ มีน้ำตาลแลคโตสเช่นเดียวกับนมวัวดังนั้นจึงไม่เหมาะกับผู้แพ้น้ำตาลแลคโตส   เพราะอาจทำให้มีอาการแน่นท้อง ท้องอืด คลื่นไส้หรือท้องเสีย เมื่อบริโภคแลคโตสเข้าสู่ร่างกาย''')

    st.subheader('นมอัลมอนด์🥜 ')
    st.subheader('𝗯𝗲𝗻𝗲𝗳𝗶𝘁👍')
    st.caption('''★ อุดมไปด้วยไขมันอิ่มเป็นตัวเลือกที่ดีสำหรับผู้ที่มีอาการแพ้แลคโตสในนมวัว
    ★ แคลอรี่ต่ำ
    
    ★ น้ำตาลต่ำ
    
    ★ วิตามินสูง
    
    ★ แหล่งแคลเซียมที่ดี
    
    ★ อุดมไปด้วยวิตามินดี
    
    ★ ไม่ใช่ผลิตภัณฑ์ที่ทำจากนมและเป็นมังสวิรัติ
    
    '''
               )
    st.subheader('𝗯𝗹𝗮𝗺𝗲👎')
    cow = Image.open('almond.jpg')
    st.image(cow)

    st.subheader('นมถั่วเหลือง🫘💛')
    st.subheader('𝗯𝗲𝗻𝗲𝗳𝗶𝘁👍')
    st.caption('''★ มีโปรตีนสูง 
    
    ★ มีวิตามินAB12,Dโพแทสเซียมและแมกนีเซียม 
    
    ★เป็นตัวเลือกที่ดีสำหรับผู้แพ้นมวัว''')
    st.subheader('𝗯𝗹𝗮𝗺𝗲👎')
    cow = Image.open('tua.jpg')
    st.image(cow)

    st.subheader(' นมน้ำข้าว🌾 ')
    st.subheader('𝗯𝗲𝗻𝗲𝗳𝗶𝘁👍')
    st.caption('''★ มีคาร์โบไฮเดรตสูง 
    
    ★ โปรตีนต่ำ ไม่มีคอเลสเตอรอล''')
    st.subheader('𝗯𝗹𝗮𝗺𝗲👎')
    cow = Image.open('right.jpg')
    st.image(cow)


    st.subheader('นมข้าวโพด🌽')
    st.subheader('𝗯𝗲𝗻𝗲𝗳𝗶𝘁👍')
    st.caption('''★ มีไฟเบอร์สูง 
    
    ★อุดมไปด้วยวิตามิน A, B และบีตาแคโรทีน''')

    st.subheader('นมมะพร้าว🥥')
    st.subheader('𝗯𝗲𝗻𝗲𝗳𝗶𝘁👍')
    st.caption('''★ มีแคลรอรี่ต่ำ
     
     ★ มีไขมันที่ดีที่ร่างกาย''')
    st.subheader('𝗯𝗹𝗮𝗺𝗲👎')
    cow = Image.open('coconut.jpg')
    st.image(cow)

    st.subheader('นมถั่วพิสทาชิโอ☘️')
    st.subheader('𝗯𝗲𝗻𝗲𝗳𝗶𝘁👍')
    st.caption('''★ มีวิตามินE แคลเซียม และใยอาหารสูง''')
    st.subheader('𝗯𝗹𝗮𝗺𝗲👎')
    st.caption('''🎈 รู้สึกคันในช่องปากหรือริมฝีปาก ผิวหนังมีผื่นแดง คลื่นไส้ อาเจียน ปวดท้อง ท้องเสีย รู้สึกไม่สบายตัว อ่อนเพลีย''')

    st.caption('''จะได้เห็นว่า นม มีประโยชน์ต่อร่างกายหลายด้าน อย่างไรก็ตามการดื่มนมมากเกินไปก็ส่งผลเสียได้ เช่น จากที่จะป้องกันโรคกระดูกพรุนก็กลับกลายเป็นเพิ่มความเสี่ยง เพราะมีโปรตีนมากเกินไปจากการดื่มนม ทำให้ร่างกายต้องปรับสมดุลในร่างกาย โดยดึงแคลเซียมในกระดูกและฟันออกมาใช้ด้วยนั่นเอง ดังนั้นควรศึกษาว่า ประเภทของนม แบบไหนเหมาะสมกับเรา และปริมาณเท่าไหร่จึงจะพอเหมาะ เพื่อให้การดื่มนมเกิดประโยชน์สูงสุดและไม่เกิดผลเสียต่อร่างกายนั่นเอง 😋🥛👍🏻''')