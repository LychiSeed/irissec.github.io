obf_table = [0, 195, 133, 70, 12, 207, 137, 74, 24, 219, 157, 94, 20, 215, 145, 82, 48, 243, 181, 118, 60, 255, 185, 122, 40, 235, 173, 110, 36, 231, 161, 98, 96, 163, 229, 38, 108, 175, 233, 42, 120, 187, 253, 62, 116, 183, 241, 50, 80, 147, 213, 22, 92, 159, 217, 26, 72, 139, 205, 14, 68, 135, 193, 2, 192, 3, 69, 134, 204, 15, 73, 138, 216, 27, 93, 158, 212, 23, 81, 146, 240, 51, 117, 182, 252, 63, 121, 186, 232, 43, 109, 174, 228, 39, 97, 162, 160, 99, 37, 230, 172, 111, 41, 234, 184, 123, 61, 254, 180, 119, 49, 242, 144, 83, 21, 214, 156, 95, 25, 218, 136, 75, 13, 206, 132, 71, 1, 194, 131, 64, 6, 197, 143, 76, 10, 201, 155, 88, 30, 221, 151, 84, 18, 209, 179, 112, 54, 245, 191, 124, 58, 249, 171, 104, 46, 237, 167, 100, 34, 225, 227, 32, 102, 165, 239, 44, 106, 169, 251, 56, 126, 189, 247, 52, 114, 177, 211, 16, 86, 149, 223, 28, 90, 153, 203, 8, 78, 141, 199, 4, 66, 129, 67, 128, 198, 5, 79, 140, 202, 9, 91, 152, 222, 29, 87, 148, 210, 17, 115, 176, 246, 53, 127, 188, 250, 57, 107, 168, 238, 45, 103, 164, 226, 33, 35, 224, 166, 101, 47, 236, 170, 105, 59, 248, 190, 125, 55, 244, 178, 113, 19, 208, 150, 85, 31, 220, 154, 89, 11, 200, 142, 77, 7, 196, 130, 65]

st = f"c254 = If(inp == 254, BitVecVal({obf_table[254]}, 32), BitVecVal({obf_table[255]}, 32))\n"
for i in range(253, -1, -1):
    st += f"c{i} = If(inp == {i}, BitVecVal({obf_table[i]}, 32), c{i + 1})\n"

print(st)