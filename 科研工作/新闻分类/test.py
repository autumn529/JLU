# blackbox_demo.py
import sys
import os

def clear_screen():
    """清屏函数"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """打印标题"""
    print("╔══════════════════════════════════════════╗")
    print("║      PYTHON 数组排序演示 - 独立窗口      ║")
    print("╚══════════════════════════════════════════╝")
    print()

def main():
    """主函数"""
    clear_screen()
    print_header()
    
    # 10个元素的数组
    arr = [64, 34, 25, 12, 22, 11, 98, 88, 7, 45]
    
    print("原始数组:")
    print(f"  {arr}")
    print("-" * 50)
    
    # 排序演示
    print("1. 升序排序:")
    asc_sorted = sorted(arr)
    print(f"   {asc_sorted}")
    print()
    
    print("2. 降序排序:")
    desc_sorted = sorted(arr, reverse=True)
    print(f"   {desc_sorted}")
    print()
    
    print("3. 原地排序 (sort()方法):")
    arr_copy = arr.copy()
    arr_copy.sort()
    print(f"   {arr_copy}")
    print()
    
    print("4. 原数组未改变:")
    print(f"   {arr}")
    print("-" * 50)
    
    # 高级功能
    print("5. 高级排序功能:")
    print(f"   按个位数排序: {sorted(arr, key=lambda x: x % 10)}")
    print(f"   按十位数排序: {sorted(arr, key=lambda x: x // 10)}")
    print(f"   按数字反转排序: {sorted(arr, key=lambda x: int(str(x)[::-1]))}")
    print()
    
    # 统计信息
    print("6. 数组统计:")
    print(f"   最大值: {max(arr)}")
    print(f"   最小值: {min(arr)}")
    print(f"   总和: {sum(arr)}")
    print(f"   平均值: {sum(arr)/len(arr):.2f}")
    print(f"   长度: {len(arr)}")
    
    print()
    print("=" * 50)
    input("按回车键退出程序...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n程序被用户中断。")
    except Exception as e:
        print(f"\n程序出错: {e}")
    finally:
        print("程序结束。")