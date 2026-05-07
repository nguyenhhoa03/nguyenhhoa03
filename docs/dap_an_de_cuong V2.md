# ĐÁP ÁN ĐỀ CƯƠNG TIN HỌC

---

## ĐỀ SỐ 1

**Mô tả:** Cơ sở dữ liệu QUANLYTHI được xây dựng nhằm phục vụ công tác quản lý thông tin thí sinh và kết quả thi. Hệ thống lưu trữ dữ liệu về thí sinh, đối tượng dự thi, các môn thi và điểm số của từng thí sinh theo từng môn.

**Các bảng:** THISINH (MaTS, Ho, Ten, NTNS, NoiSinh, MaDT) | DOITUONG (MaDT, TenDT) | MONHOC (MaMon, TenMon) | DIEM (MaTS, MaMon, Diem)

---

```
Câu 1:
In danh sách gồm: Ho, Ten, NTNS, NoiSinh. Chỉ hiển thị những thí sinh ở Bến Tre và Long An. Danh sách sắp xếp giảm dần theo tên.

SELECT THISINH.Ho, THISINH.Ten, THISINH.NTNS, THISINH.NoiSinh
FROM THISINH
WHERE THISINH.NoiSinh = 'Bến Tre'
   OR THISINH.NoiSinh = 'Long An'
ORDER BY THISINH.Ten DESC;
```

```
Câu 2:
In danh sách gồm: Ho, Ten, NTNS, NoiSinh, điểm thi các môn. Chỉ hiển thị những thí sinh có ít nhất 1 môn đạt điểm ≥ 9.

SELECT DISTINCT THISINH.Ho, THISINH.Ten, THISINH.NTNS, THISINH.NoiSinh, DIEM.Diem
FROM THISINH
INNER JOIN DIEM ON THISINH.MaTS = DIEM.MaTS
WHERE DIEM.Diem >= 9;
```

```
Câu 3:
In danh sách gồm: Ho, Ten, NoiSinh, TenDT. Chỉ hiển thị những thí sinh thuộc diện: "Đối tượng thuộc diện chính sách".

SELECT THISINH.Ho, THISINH.Ten, THISINH.NoiSinh, DOITUONG.TenDT
FROM THISINH
INNER JOIN DOITUONG ON THISINH.MaDT = DOITUONG.MaDT
WHERE DOITUONG.TenDT = 'Đối tượng thuộc diện chính sách';
```

```
Câu 4:
In danh sách gồm: Ho, Ten, NoiSinh, TenDT, trung bình điểm 3 môn. Chỉ hiển thị những thí sinh có điểm trung bình ≥ 6.0.

SELECT THISINH.Ho, THISINH.Ten, THISINH.NoiSinh, DOITUONG.TenDT, AVG(DIEM.Diem)
FROM THISINH
INNER JOIN DOITUONG ON THISINH.MaDT = DOITUONG.MaDT
INNER JOIN DIEM ON THISINH.MaTS = DIEM.MaTS
GROUP BY THISINH.MaTS
HAVING AVG(DIEM.Diem) >= 6.0;
```

```
Câu 5:
In danh sách gồm: Ho, Ten, NTNS, NoiSinh. Chỉ hiển thị những thí sinh ở TP.HCM sinh năm 1983.

SELECT THISINH.Ho, THISINH.Ten, THISINH.NTNS, THISINH.NoiSinh
FROM THISINH
WHERE THISINH.NoiSinh = 'TP.HCM' AND YEAR(THISINH.NTNS) = 1983;
```

```
Câu 6:
In danh sách gồm: Ho, Ten, NTNS, NoiSinh, TenDT. Chỉ hiển thị những thí sinh sinh ở Bến Tre hoặc TP.HCM và thuộc diện "Cán bộ, công nhân viên chức nhà nước". Danh sách sắp xếp tăng dần theo tên.

SELECT THISINH.Ho, THISINH.Ten, THISINH.NTNS, THISINH.NoiSinh, DOITUONG.TenDT
FROM THISINH
INNER JOIN DOITUONG ON THISINH.MaDT = DOITUONG.MaDT
WHERE (THISINH.NoiSinh = 'Bến Tre' OR THISINH.NoiSinh = 'TP.HCM')
  AND DOITUONG.TenDT = 'Cán bộ, công nhân viên chức nhà nước'
ORDER BY THISINH.Ten ASC;
```

```
Câu 7:
In danh sách gồm: Ho, Ten, NoiSinh, TenDT. Chỉ hiển thị những thí sinh không thuộc diện "Thí sinh tự do".

SELECT THISINH.Ho, THISINH.Ten, THISINH.NoiSinh, DOITUONG.TenDT
FROM THISINH
INNER JOIN DOITUONG ON THISINH.MaDT = DOITUONG.MaDT
WHERE DOITUONG.TenDT <> 'Thí sinh tự do';
```

```
Câu 8:
In danh sách gồm: Ho, Ten, NoiSinh, TenDT, tổng điểm 3 môn. Chỉ hiển thị những thí sinh có tổng điểm ≥ 15 và không có môn nào dưới 5 điểm.

SELECT THISINH.Ho, THISINH.Ten, THISINH.NoiSinh, DOITUONG.TenDT, SUM(DIEM.Diem)
FROM THISINH
INNER JOIN DOITUONG ON THISINH.MaDT = DOITUONG.MaDT
INNER JOIN DIEM ON THISINH.MaTS = DIEM.MaTS
GROUP BY THISINH.MaTS
HAVING SUM(DIEM.Diem) >= 15 AND MIN(DIEM.Diem) >= 5;
```

```
Câu 9:
In danh sách gồm: Ho, Ten, NTNS, NoiSinh. Chỉ hiển thị những thí sinh ở Long An hoặc TP.HCM, sinh năm 1982. Danh sách sắp xếp tăng dần theo tên.

SELECT THISINH.Ho, THISINH.Ten, THISINH.NTNS, THISINH.NoiSinh
FROM THISINH
WHERE (THISINH.NoiSinh = 'Long An' OR THISINH.NoiSinh = 'TP.HCM') AND YEAR(THISINH.NTNS) = 1982
ORDER BY THISINH.Ten ASC;
```

```
Câu 10:
In danh sách gồm: Ho, Ten, NoiSinh, TenDT. Chỉ hiển thị những thí sinh thuộc diện "Cán bộ, công nhân viên chức nhà nước" và có ít nhất 1 môn dưới 5 điểm.

SELECT DISTINCT THISINH.Ho, THISINH.Ten, THISINH.NoiSinh, DOITUONG.TenDT
FROM THISINH
INNER JOIN DOITUONG ON THISINH.MaDT = DOITUONG.MaDT
INNER JOIN DIEM ON THISINH.MaTS = DIEM.MaTS
WHERE DOITUONG.TenDT = 'Cán bộ, công nhân viên chức nhà nước' AND DIEM.Diem < 5;
```

```
Câu 11:
In danh sách gồm: Ho, Ten, NoiSinh, tổng điểm 3 môn. Chỉ hiển thị những thí sinh ở Bến Tre và có tổng điểm < 18.

SELECT THISINH.Ho, THISINH.Ten, THISINH.NoiSinh, SUM(DIEM.Diem)
FROM THISINH
INNER JOIN DIEM ON THISINH.MaTS = DIEM.MaTS
WHERE THISINH.NoiSinh = 'Bến Tre'
GROUP BY THISINH.MaTS
HAVING SUM(DIEM.Diem) < 18;
```

```
Câu 12:
In danh sách gồm: Ho, Ten, NoiSinh, TenDT. Chỉ hiển thị những thí sinh không thuộc diện chính sách và có tất cả các môn ≥ 7 điểm.

SELECT THISINH.Ho, THISINH.Ten, THISINH.NoiSinh, DOITUONG.TenDT
FROM THISINH
INNER JOIN DOITUONG ON THISINH.MaDT = DOITUONG.MaDT
INNER JOIN DIEM ON THISINH.MaTS = DIEM.MaTS
WHERE DOITUONG.TenDT <> 'Đối tượng thuộc diện chính sách'
GROUP BY THISINH.MaTS, THISINH.Ho, THISINH.Ten, THISINH.NoiSinh, DOITUONG.TenDT
HAVING MIN(DIEM.Diem) >= 7;
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

SELECT NHANVIEN.Ho, NHANVIEN.Ten, CHUCVU.TenCV, PHONGBAN.TenPB, NHANVIEN.LuongCB
FROM NHANVIEN
INNER JOIN CHUCVU ON NHANVIEN.MaCV = CHUCVU.MaCV
INNER JOIN PHONGBAN ON NHANVIEN.MaPB = PHONGBAN.MaPB
ORDER BY CHUCVU.TenCV ASC;
```

```
Câu 2:
In danh sách gồm: Ho, Ten, TenCV, TenPB. Chỉ hiển thị những nhân viên thuộc phòng Hành Chánh có thu nhập từ 1.350.000 trở lên. (Thu nhập = LuongCB * NgayCong)

SELECT NHANVIEN.Ho, NHANVIEN.Ten, CHUCVU.TenCV, PHONGBAN.TenPB
FROM NHANVIEN
INNER JOIN CHUCVU ON NHANVIEN.MaCV = CHUCVU.MaCV
INNER JOIN PHONGBAN ON NHANVIEN.MaPB = PHONGBAN.MaPB
WHERE PHONGBAN.TenPB = 'Hành Chánh'
  AND (NHANVIEN.LuongCB * NHANVIEN.NgayCong) >= 1350000;
```

```
Câu 3:
In danh sách gồm: Ho, Ten, TenCV, TenPB, LuongCB. Chỉ hiển thị những người có LuongCB từ 20.000 đến 35.000 thuộc phòng Tài Vụ và Sản Xuất.

SELECT NHANVIEN.Ho, NHANVIEN.Ten, CHUCVU.TenCV, PHONGBAN.TenPB, NHANVIEN.LuongCB
FROM NHANVIEN
INNER JOIN CHUCVU ON NHANVIEN.MaCV = CHUCVU.MaCV
INNER JOIN PHONGBAN ON NHANVIEN.MaPB = PHONGBAN.MaPB
WHERE NHANVIEN.LuongCB >= 20000 AND NHANVIEN.LuongCB <= 35000
  AND (PHONGBAN.TenPB = 'Tài Vụ' OR PHONGBAN.TenPB = 'Sản Xuất');
```

```
Câu 4:
In danh sách những người phải nộp thuế gồm: Ho, Ten, TenCV, TenPB, LuongCB. Chỉ hiển thị những người có thu nhập từ 1.000.000 trở lên. (Thu nhập = LuongCB * NgayCong)

SELECT NHANVIEN.Ho, NHANVIEN.Ten, CHUCVU.TenCV, PHONGBAN.TenPB, NHANVIEN.LuongCB
FROM NHANVIEN
INNER JOIN CHUCVU ON NHANVIEN.MaCV = CHUCVU.MaCV
INNER JOIN PHONGBAN ON NHANVIEN.MaPB = PHONGBAN.MaPB
WHERE (NHANVIEN.LuongCB * NHANVIEN.NgayCong) >= 1000000;
```

```
Câu 5:
In danh sách gồm: Ho, Ten, TenCV, NgayCong, LuongCB. Danh sách được sắp xếp tăng dần theo ChucVu. Chỉ hiển thị những người có số ngày làm việc từ 22 đến 26 ngày.

SELECT NHANVIEN.Ho, NHANVIEN.Ten, CHUCVU.TenCV, NHANVIEN.NgayCong, NHANVIEN.LuongCB
FROM NHANVIEN
INNER JOIN CHUCVU ON NHANVIEN.MaCV = CHUCVU.MaCV
WHERE NHANVIEN.NgayCong >= 22 AND NHANVIEN.NgayCong <= 26
ORDER BY CHUCVU.TenCV ASC;
```

```
Câu 6:
In danh sách trợ cấp gồm: Ho, Ten, TenCV, TenPB. Chỉ hiển thị những nhân viên thuộc phòng Hành Chánh hoặc Sản Xuất có thu nhập dưới 1.350.000. (Thu nhập = LuongCB * NgayCong)

SELECT NHANVIEN.Ho, NHANVIEN.Ten, CHUCVU.TenCV, PHONGBAN.TenPB
FROM NHANVIEN
INNER JOIN CHUCVU ON NHANVIEN.MaCV = CHUCVU.MaCV
INNER JOIN PHONGBAN ON NHANVIEN.MaPB = PHONGBAN.MaPB
WHERE (PHONGBAN.TenPB = 'Hành Chánh' OR PHONGBAN.TenPB = 'Sản Xuất')
  AND (NHANVIEN.LuongCB * NHANVIEN.NgayCong) < 1350000;
```

```
Câu 7:
In danh sách gồm: Ho, Ten, TenCV, TenPB, LuongCB. Chỉ hiển thị những người có LuongCB từ 20.000 đến 35.000 và không giữ chức vụ là GD hoặc PG, hoặc TP.

SELECT NHANVIEN.Ho, NHANVIEN.Ten, CHUCVU.TenCV, PHONGBAN.TenPB, NHANVIEN.LuongCB
FROM NHANVIEN
INNER JOIN CHUCVU ON NHANVIEN.MaCV = CHUCVU.MaCV
INNER JOIN PHONGBAN ON NHANVIEN.MaPB = PHONGBAN.MaPB
WHERE NHANVIEN.LuongCB >= 20000 AND NHANVIEN.LuongCB <= 35000
  AND CHUCVU.TenCV <> 'GD'
  AND CHUCVU.TenCV <> 'PG'
  AND CHUCVU.TenCV <> 'TP';
```

```
Câu 8:
In danh sách những người hưởng trợ cấp gồm: Ho, Ten, TenCV, TenPB, LuongCB. Chỉ hiển thị những người có thu nhập từ 390.000 trở xuống. (Thu nhập = LuongCB * NgayCong)

SELECT NHANVIEN.Ho, NHANVIEN.Ten, CHUCVU.TenCV, PHONGBAN.TenPB, NHANVIEN.LuongCB
FROM NHANVIEN
INNER JOIN CHUCVU ON NHANVIEN.MaCV = CHUCVU.MaCV
INNER JOIN PHONGBAN ON NHANVIEN.MaPB = PHONGBAN.MaPB
WHERE (NHANVIEN.LuongCB * NHANVIEN.NgayCong) <= 390000;
```

```
Câu 9:
In danh sách gồm: Ho, Ten, TenCV, NgayCong, LuongCB. Chỉ hiển thị những nhân viên có số ngày công từ 20 đến 25 ngày. Danh sách sắp xếp tăng dần theo tên chức vụ.

SELECT NHANVIEN.Ho, NHANVIEN.Ten, CHUCVU.TenCV, NHANVIEN.NgayCong, NHANVIEN.LuongCB
FROM NHANVIEN
INNER JOIN CHUCVU ON NHANVIEN.MaCV = CHUCVU.MaCV
WHERE NHANVIEN.NgayCong >= 20 AND NHANVIEN.NgayCong <= 25
ORDER BY CHUCVU.TenCV ASC;
```

```
Câu 10:
In danh sách gồm: Ho, Ten, TenCV, TenPB. Chỉ hiển thị những nhân viên thuộc phòng Sản Xuất hoặc Tài Vụ và có thu nhập < 1.200.000.

SELECT NHANVIEN.Ho, NHANVIEN.Ten, CHUCVU.TenCV, PHONGBAN.TenPB
FROM NHANVIEN
INNER JOIN CHUCVU ON NHANVIEN.MaCV = CHUCVU.MaCV
INNER JOIN PHONGBAN ON NHANVIEN.MaPB = PHONGBAN.MaPB
WHERE (PHONGBAN.TenPB = 'Sản Xuất' OR PHONGBAN.TenPB = 'Tài Vụ')
  AND (NHANVIEN.LuongCB * NHANVIEN.NgayCong) < 1200000;
```
