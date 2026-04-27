from checkmate import checkmate
 
 
def main():
    # ตัวอย่างที่ 1: R อยู่ในแนวเดียวกับ K → Success
    board = """\
bbbb
rrrr
..p.
p.k."""
    checkmate(board)
 
 
if __name__ == "__main__":
    main()
 
 # K Q R P B