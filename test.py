"""""
        if(k == 0):
            hrana_Up = slice(current, current+2*k+1)
            B[i+k:i-k-2:-1, j+k] = b[hrana_Up]
            current += 2*k+1
            
            hrana_Left = slice(current, current+2*k+2)
            B[i-k-1, j+k:j-k-2:-1] = b[hrana_Left]
            current += 2*k+2
            
            hrana_Down = slice(current, current+2*k+2)
            B[i-k:i+k+2, j-k-1] = b[hrana_Down]
            current += 2*k+2
            
            hrana_Right = slice(current, current+2*k+2)
            B[i+k+1, j-k:j+k+2 ] = b[hrana_Right]
            current += 2*k+2

            continue
        """""
        