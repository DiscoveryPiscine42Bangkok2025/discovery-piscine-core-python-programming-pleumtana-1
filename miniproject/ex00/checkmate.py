def checkmate(board):
    """
    รับกระดานหมากรุกในรูปแบบ string หลายบรรทัด
    แล้วตรวจสอบว่าพระราชา (K) ถูกคุกคาม (in check) หรือไม่
    พิมพ์ "Success" ถ้าถูกคุกคาม, "Fail" ถ้าไม่ถูกคุกคาม
    """
    if not isinstance(board, str):
        return
 
    rows = board.split('\n')
 
    # ตรวจสอบว่าเป็นกระดานสี่เหลี่ยมจัตุรัสหรือไม่
    size = len(rows)
    if size == 0:
        return
    for row in rows:
        if len(row) != size:
            print("Error: board")
            return
        

    VALID_PIECES = {'K', 'Q', 'R', 'B', 'P', '.'}
    for row in rows:
        for ch in row:
            if ch not in VALID_PIECES:
                print("Error: Pieces")
                return
            

    # หาตำแหน่งของพระราชา (K)
    king_pos = None
    for r in range(size):
        for c in range(size):
            if rows[r][c] == 'K':
                king_pos = (r, c)
                break
        if king_pos:
            break
 
    if king_pos is None:
        print("Error: No ok")
        return
 

    # ตรวจสอบว่ามี K มากกว่า 1 ตัวหรือไม่
    king_count = sum(ch in 'K' for row in rows for ch in row)
    if king_count > 1:
        print("Error: K++")
        return
    
    kr, kc = king_pos
    # ตรวจสอบ Rook (R) และ Queen (Q) ในแนวแถวและคอลัมน์
    # ทิศทาง: ขึ้น, ลง, ซ้าย, ขวา
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            piece = rows[r][c]
            if piece == 'R' or piece == 'Q':
                print("Success")
                return
            elif piece != '.':
                break  # มีตัวหมากอื่นขวางอยู่
            r += dr
            c += dc
 
    # ตรวจสอบ Bishop (B) และ Queen (Q) ในแนวทแยง
    for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            piece = rows[r][c]
            if piece == 'B' or piece == 'Q':
                print("Success")
                return
            elif piece != '.':
                break
            r += dr
            c += dc
 
    # ตรวจสอบ Pawn (P) — เบี้ยโจมตีแนวทแยงขึ้นด้านบน
    # ดังนั้นจากมุมมองของ K ให้มองหา P ที่อยู่แถวล่าง (+1) ซ้ายและขวา
    for dr, dc in [(1, -1), (1, 1)]:
        r, c = kr + dr, kc + dc
        if 0 <= r < size and 0 <= c < size:
            if rows[r][c] == 'P':
                print("Success")
                return
 
    print("Fail")