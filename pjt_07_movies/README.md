## ver2_영화

<details>
  <summary>models.py</summary>

![alt text](image-11.png)
</details>


<details>
  <summary>urls.py</summary>

![alt text](image-12.png)
</details>

<details>
  <summary>serializers.py</summary>

![alt text](image-9.png)

![alt text](image-10.png)
</details>


<details>
  <summary>views.py</summary>

![alt text](image-13.png)

![alt text](image-14.png)
</details>


### 배우 목록
<details>
  <summary>전체 배우 목록 제공</summary>
- [GET] http://127.0.0.1:8000/api/v1/actors/

![alt text](image.png)
</details>


<details>
  <summary>단일 배우 정보 제공</summary>
- [GET] http://127.0.0.1:8000/api/v1/actors/1/

![alt text](image-1.png)
</details>

---

### 영화 목록
<details>
  <summary>전체 영화 목록 제공</summary>
- [GET] http://127.0.0.1:8000/api/v1/movies/

![alt text](image-2.png)
</details>


<details>
  <summary>단일 영화 목록 제공</summary>
- [GET] http://127.0.0.1:8000/api/v1/movies/1/

![alt text](image-3.png)
</details>

---

### 리뷰 목록
<details>
  <summary>전체 리뷰 목록 제공</summary>
- [GET] http://127.0.0.1:8000/api/v1/reviews/

![alt text](image-4.png)
</details>


<details>
  <summary>단일 리뷰 조회</summary>
- [GET] http://127.0.0.1:8000/api/v1/reviews/1/

![alt text](image-5.png)
</details>


<details>
  <summary>단일 리뷰 수정</summary>
- [PUT] http://127.0.0.1:8000/api/v1/reviews/3/

![alt text](image-6.png)
</details>


<details>
  <summary>단일 리뷰 삭제</summary>
- [DELETE] http://127.0.0.1:8000/api/v1/reviews/3/

![alt text](image-7.png)
</details>


<details>
  <summary>리뷰 생성</summary>
- [POST] http://127.0.0.1:8000/api/v1/movies/3/reviews/

![alt text](image-8.png)
</details>
