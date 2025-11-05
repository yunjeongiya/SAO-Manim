작업 완료 프로세스 실행 (작업 정리, 일지 작성, 요구사항 검토, 커밋, 최종 보고)

---

# /finish - 작업 완료 프로세스

현재 진행 중인 Feature 작업을 완료하고 문서화합니다.

## 실행 순서

### 1. 현재 작업 확인
- `docs/features/INDEX.md`에서 IN_PROGRESS 상태의 Feature 찾기
- 해당 Feature의 README.md 확인

### 2. 작업 정리
- [ ] 모든 Todo 완료 확인
- [ ] 테스트 실행 (해당되는 경우)
- [ ] 불필요한 주석/로그 제거

### 3. 일지 작성
- `docs/daily_work_summary/YYYY-MM-DD.md` 생성/업데이트
- 작업 내용, 주요 변경사항, 배운 점 기록

### 4. Feature 문서 업데이트
- Feature의 README.md에 완료일 기록
- 스크린샷/결과물이 있다면 추가
- INDEX.md에서 상태를 COMPLETED로 변경

### 5. Git 커밋
- 수정한 파일만 명시적으로 add
- 의미 있는 커밋 메시지 작성
- 형식: `feat: [Feature ID] - 간단한 설명`

### 6. 최종 보고
사용자에게 다음 내용 보고:
- ✅ 완료된 작업 요약
- 📝 작성된 문서 링크
- 🔗 커밋 해시
- 💡 다음 단계 제안 (있는 경우)

## 사용 예시
```
사용자: /finish
Claude: [위 프로세스 실행]
```
