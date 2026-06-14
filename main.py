# main.py
from pranai_core import PranAICore
from pranai_inventor import PranAIInventor
from pranai_evaluator import PranAIEvaluator

def main():
    print("=" * 65)
    print("🚀 VIDER PranAI ระบบค้นหาและสร้างสรรค์เทคโนโลยี")
    print("🔑 คีย์เปิดใช้งาน: ViderPranAI244")
    print("⚙️  แกนหลัก: Qvnt‑SC 1.7.1 Basic")
    print("=" * 65)

    try:
        core = PranAICore()
        inventor = PranAIInventor(core)
        print("\n✅ ระบบพร้อมทำงานเต็มรูปแบบ")

        # ตัวอย่างการใช้งาน
        topic = "ระบบกักเก็บพลังงานประสิทธิภาพสูง"
        result = inventor.invent_technology(topic)

        print("\n📋 ผลลัพธ์การประดิษฐ์:")
        for key, value in result.items():
            print(f"• {key}: {value}")

    except PermissionError as e:
        print(f"\n❌ ไม่สามารถเปิดใช้งานได้: {e}")

if __name__ == "__main__":
    main()
