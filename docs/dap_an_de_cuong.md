# ĐÁP ÁN ĐỀ CƯƠNG TIN HỌC

---

## ĐỀ SỐ 1

**Mô tả:** Cơ sở dữ liệu QUANLYTHI được xây dựng nhằm phục vụ công tác quản lý thông tin thí sinh và kết quả thi. Hệ thống lưu trữ dữ liệu về thí sinh, đối tượng dự thi, các môn thi và điểm số của từng thí sinh theo từng môn.

**Các bảng:** THISINH (MaTS, Ho, Ten, NTNS, NoiSinh, MaDT) | DOITUONG (MaDT, TenDT) | MONHOC (MaMon, TenMon) | DIEM (MaTS, MaMon, Diem)

---

```
Câu 1:
In danh sách gồm: Ho, Ten, NTNS, NoiSinh. Chỉ hiển thị những thí sinh ở Bến Tre và Long An. Danh sách sắp xếp giảm dần theo tên.

SELECT Ho, Ten, NTNS, NoiSinh
FROM THISINH
WHERE NoiSinh = 'Bến Tre'
   OR NoiSinh = 'Long An'
ORDER BY Ten DESC;
```

```
Câu 2:
In danh sách gồm: Ho, Ten, NTNS, NoiSinh, điểm thi các môn. Chỉ hiển thị những thí sinh có ít nhất 1 môn đạt điểm ≥ 9.

SELECT DISTINCT ts.Ho, ts.Ten, ts.NTNS, ts.NoiSinh, d.Diem
FROM THISINH ts
INNER JOIN DIEM d ON ts.MaTS = d.MaTS
WHERE d.Diem >= 9;
```

```
Câu 3:
In danh sách gồm: Ho, Ten, NoiSinh, TenDT. Chỉ hiển thị những thí sinh thuộc diện: "Đối tượng thuộc diện chính sách".

SELECT ts.Ho, ts.Ten, ts.NoiSinh, dt.TenDT
FROM THISINH ts
INNER JOIN DOITUONG dt ON ts.MaDT = dt.MaDT
WHERE dt.TenDT = 'Đối tượng thuộc diện chính sách';
```

```
Câu 4:
In danh sách gồm: Ho, Ten, NoiSinh, TenDT, trung bình điểm 3 môn. Chỉ hiển thị những thí sinh có điểm trung bình ≥ 6.0.

SELECT ts.Ho, ts.Ten, ts.NoiSinh, dt.TenDT, AVG(d.Diem) AS TongDiem
FROM THISINH ts
INNER JOIN DOITUONG dt ON ts.MaDT = dt.MaDT
INNER JOIN DIEM d ON ts.MaTS = d.MaTS
GROUP BY ts.MaTS
HAVING AVG(d.Diem) >= 6.0;
```

```
Câu 5:
In danh sách gồm: Ho, Ten, NTNS, NoiSinh. Chỉ hiển thị những thí sinh ở TP.HCM sinh năm 1983.

SELECT Ho, Ten, NTNS, NoiSinh
FROM THISINH
WHERE NoiSinh = 'TP.HCM' AND YEAR(NTNS) = 1983;
```

```
Câu 6:
In danh sách gồm: Ho, Ten, NTNS, NoiSinh, TenDT. Chỉ hiển thị những thí sinh sinh ở Bến Tre hoặc TP.HCM và thuộc diện "Cán bộ, công nhân viên chức nhà nước". Danh sách sắp xếp tăng dần theo tên.

SELECT ts.Ho, ts.Ten, ts.NTNS, ts.NoiSinh, dt.TenDT
FROM THISINH ts
INNER JOIN DOITUONG dt ON ts.MaDT = dt.MaDT
WHERE (ts.NoiSinh = 'Bến Tre' OR ts.NoiSinh = 'TP.HCM')
  AND dt.TenDT = 'Cán bộ, công nhân viên chức nhà nước'
ORDER BY ts.Ten ASC;
```

```
Câu 7:
In danh sách gồm: Ho, Ten, NoiSinh, TenDT. Chỉ hiển thị những thí sinh không thuộc diện "Thí sinh tự do".

SELECT ts.Ho, ts.Ten, ts.NoiSinh, dt.TenDT
FROM THISINH ts
INNER JOIN DOITUONG dt ON ts.MaDT = dt.MaDT
WHERE dt.TenDT <> 'Thí sinh tự do';
```

```
Câu 8:
In danh sách gồm: Ho, Ten, NoiSinh, TenDT, tổng điểm 3 môn. Chỉ hiển thị những thí sinh có tổng điểm ≥ 15 và không có môn nào dưới 5 điểm.

SELECT ts.Ho, ts.Ten, ts.NoiSinh, dt.TenDT, SUM(d.Diem) AS TongDiem
FROM THISINH ts
INNER JOIN DOITUONG dt ON ts.MaDT = dt.MaDT
INNER JOIN DIEM d ON ts.MaTS = d.MaTS
GROUP BY ts.MaTS
HAVING SUM(d.Diem) >= 15 AND MIN(d.Diem) >= 5;
```

```
Câu 9:
In danh sách gồm: Ho, Ten, NTNS, NoiSinh. Chỉ hiển thị những thí sinh ở Long An hoặc TP.HCM, sinh năm 1982. Danh sách sắp xếp tăng dần theo tên.

SELECT Ho, Ten, NTNS, NoiSinh
FROM THISINH
WHERE (NoiSinh = 'Long An' OR NoiSinh = 'TP.HCM') AND YEAR(NTNS) = 1982
ORDER BY Ten ASC;
```

```
Câu 10:
In danh sách gồm: Ho, Ten, NoiSinh, TenDT. Chỉ hiển thị những thí sinh thuộc diện "Cán bộ, công nhân viên chức nhà nước" và có ít nhất 1 môn dưới 5 điểm.

SELECT DISTINCT ts.Ho, ts.Ten, ts.NoiSinh, dt.TenDT
FROM THISINH ts
INNER JOIN DOITUONG dt ON ts.MaDT = dt.MaDT
INNER JOIN DIEM d ON ts.MaTS = d.MaTS
WHERE dt.TenDT = 'Cán bộ, công nhân viên chức nhà nước' AND d.Diem < 5;
```

```
Câu 11:
In danh sách gồm: Ho, Ten, NoiSinh, tổng điểm 3 môn. Chỉ hiển thị những thí sinh ở Bến Tre và có tổng điểm < 18.

SELECT ts.Ho, ts.Ten, ts.NoiSinh, SUM(d.Diem) AS TongDiem
FROM THISINH ts
INNER JOIN DIEM d ON ts.MaTS = d.MaTS
WHERE ts.NoiSinh = 'Bến Tre'
GROUP BY ts.MaTS
HAVING SUM(d.Diem) < 18;
```

```
Câu 12:
In danh sách gồm: Ho, Ten, NoiSinh, TenDT. Chỉ hiển thị những thí sinh không thuộc diện chính sách và có tất cả các môn ≥ 7 điểm.

SELECT ts.Ho, ts.Ten, ts.NoiSinh, dt.TenDT
FROM THISINH ts
INNER JOIN DOITUONG dt ON ts.MaDT = dt.MaDT
INNER JOIN DIEM d ON ts.MaTS = d.MaTS
WHERE dt.TenDT <> 'Đối tượng thuộc diện chính sách'
GROUP BY ts.MaTS, ts.Ho, ts.Ten, ts.NoiSinh, dt.TenDT
HAVING MIN(d.Diem) >= 7;
```

---

## ĐỀ SỐ 2

**Mô tả:** Cơ sở dữ liệu NHANSU được xây dựng nhằm phục vụ công tác quản lý thông tin nhân viên trong một cơ quan hoặc doanh nghiệp. Hệ thống lưu trữ dữ liệu về nhân viên, phòng ban và chức vụ, đồng thời hỗ trợ tính toán thu nhập dựa trên lương cơ bản và số ngày công.

**Các bảng:** NHANVIEN (MaNV, Ho, Ten, MaCV, MaPB, LuongCB, NgayCong) | PHONGBAN (MaPB, TenPB) | CHUCVU (MaCV, TenCV)

**Công thức:** ThuNhap = LuongCB × NgayCong

---

```
Câu 1:
In danh sách gồm: Ho, Ten, TenCV, TenPB, LuongCB. Danh sách được sắp xếp tăng dần theo TenCV.

SELECT nv.Ho, nv.Ten, cv.TenCV AS ChucVu, pb.TenPB, nv.LuongCB
FROM NHANVIEN nv
INNER JOIN CHUCVU cv ON nv.MaCV = cv.MaCV
INNER JOIN PHONGBAN pb ON nv.MaPB = pb.MaPB
ORDER BY cv.TenCV ASC;
```

```
Câu 2:
In danh sách gồm: Ho, Ten, TenCV, TenPB. Chỉ hiển thị những nhân viên thuộc phòng Hành Chánh có thu nhập từ 1.350.000 trở lên. (Thu nhập = LuongCB * NgayCong)

SELECT nv.Ho, nv.Ten, cv.TenCV AS ChucVu, pb.TenPB
FROM NHANVIEN nv
INNER JOIN CHUCVU cv ON nv.MaCV = cv.MaCV
INNER JOIN PHONGBAN pb ON nv.MaPB = pb.MaPB
WHERE pb.TenPB = 'Hành Chánh'
  AND (nv.LuongCB * nv.NgayCong) >= 1350000;
```

```
Câu 3:
In danh sách gồm: Ho, Ten, TenCV, TenPB, LuongCB. Chỉ hiển thị những người có LuongCB từ 20.000 đến 35.000 thuộc phòng Tài Vụ và Sản Xuất.

SELECT nv.Ho, nv.Ten, cv.TenCV AS ChucVu, pb.TenPB, nv.LuongCB
FROM NHANVIEN nv
INNER JOIN CHUCVU cv ON nv.MaCV = cv.MaCV
INNER JOIN PHONGBAN pb ON nv.MaPB = pb.MaPB
WHERE nv.LuongCB >= 20000 AND nv.LuongCB <= 35000
  AND (pb.TenPB = 'Tài Vụ' OR pb.TenPB = 'Sản Xuất');
```

```
Câu 4:
In danh sách những người phải nộp thuế gồm: Ho, Ten, TenCV, TenPB, LuongCB. Chỉ hiển thị những người có thu nhập từ 1.000.000 trở lên. (Thu nhập = LuongCB * NgayCong)

SELECT nv.Ho, nv.Ten, cv.TenCV AS ChucVu, pb.TenPB, nv.LuongCB
FROM NHANVIEN nv
INNER JOIN CHUCVU cv ON nv.MaCV = cv.MaCV
INNER JOIN PHONGBAN pb ON nv.MaPB = pb.MaPB
WHERE (nv.LuongCB * nv.NgayCong) >= 1000000;
```

```
Câu 5:
In danh sách gồm: Ho, Ten, TenCV, NgayCong, LuongCB. Danh sách được sắp xếp tăng dần theo ChucVu. Chỉ hiển thị những người có số ngày làm việc từ 22 đến 26 ngày.

SELECT nv.Ho, nv.Ten, cv.TenCV AS ChucVu, nv.NgayCong, nv.LuongCB
FROM NHANVIEN nv
INNER JOIN CHUCVU cv ON nv.MaCV = cv.MaCV
WHERE nv.NgayCong >= 22 AND nv.NgayCong <= 26
ORDER BY cv.TenCV ASC;
```

```
Câu 6:
In danh sách trợ cấp gồm: Ho, Ten, TenCV, TenPB. Chỉ hiển thị những nhân viên thuộc phòng Hành Chánh hoặc Sản Xuất có thu nhập dưới 1.350.000. (Thu nhập = LuongCB * NgayCong)

SELECT nv.Ho, nv.Ten, cv.TenCV AS ChucVu, pb.TenPB
FROM NHANVIEN nv
INNER JOIN CHUCVU cv ON nv.MaCV = cv.MaCV
INNER JOIN PHONGBAN pb ON nv.MaPB = pb.MaPB
WHERE (pb.TenPB = 'Hành Chánh' OR pb.TenPB = 'Sản Xuất')
  AND (nv.LuongCB * nv.NgayCong) < 1350000;
```

```
Câu 7:
In danh sách gồm: Ho, Ten, TenCV, TenPB, LuongCB. Chỉ hiển thị những người có LuongCB từ 20.000 đến 35.000 và không giữ chức vụ là GD hoặc PG, hoặc TP.

SELECT nv.Ho, nv.Ten, cv.TenCV AS ChucVu, pb.TenPB, nv.LuongCB
FROM NHANVIEN nv
INNER JOIN CHUCVU cv ON nv.MaCV = cv.MaCV
INNER JOIN PHONGBAN pb ON nv.MaPB = pb.MaPB
WHERE nv.LuongCB >= 20000 AND nv.LuongCB <= 35000
  AND cv.TenCV <> 'GD'
  AND cv.TenCV <> 'PG'
  AND cv.TenCV <> 'TP';
```

```
Câu 8:
In danh sách những người hưởng trợ cấp gồm: Ho, Ten, TenCV, TenPB, LuongCB. Chỉ hiển thị những người có thu nhập từ 390.000 trở xuống. (Thu nhập = LuongCB * NgayCong)

SELECT nv.Ho, nv.Ten, cv.TenCV AS ChucVu, pb.TenPB, nv.LuongCB
FROM NHANVIEN nv
INNER JOIN CHUCVU cv ON nv.MaCV = cv.MaCV
INNER JOIN PHONGBAN pb ON nv.MaPB = pb.MaPB
WHERE (nv.LuongCB * nv.NgayCong) <= 390000;
```

```
Câu 9:
In danh sách gồm: Ho, Ten, TenCV, NgayCong, LuongCB. Chỉ hiển thị những nhân viên có số ngày công từ 20 đến 25 ngày. Danh sách sắp xếp tăng dần theo tên chức vụ.

SELECT nv.Ho, nv.Ten, cv.TenCV AS ChucVu, nv.NgayCong, nv.LuongCB
FROM NHANVIEN nv
INNER JOIN CHUCVU cv ON nv.MaCV = cv.MaCV
WHERE nv.NgayCong >= 20 AND nv.NgayCong <= 25
ORDER BY cv.TenCV ASC;
```

```
Câu 10:
In danh sách gồm: Ho, Ten, TenCV, TenPB. Chỉ hiển thị những nhân viên thuộc phòng Sản Xuất hoặc Tài Vụ và có thu nhập < 1.200.000.

SELECT nv.Ho, nv.Ten, cv.TenCV AS ChucVu, pb.TenPB
FROM NHANVIEN nv
INNER JOIN CHUCVU cv ON nv.MaCV = cv.MaCV
INNER JOIN PHONGBAN pb ON nv.MaPB = pb.MaPB
WHERE (pb.TenPB = 'Sản Xuất' OR pb.TenPB = 'Tài Vụ')
  AND (nv.LuongCB * nv.NgayCong) < 1200000;
```
