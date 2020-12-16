# &#127876;	Wish_UR_Merry_Christmas &#127876;
코로나는 정말 많은 걸 바꿔놓았어요,,,:( 하지만 우리는 언텍트 시대에 걸맞게 코딩으로 트리를 만들어서 크리스마스를 즐겨봅시다! 4개월간 갈고닦은 파이썬 실력을 뽐내보아요 :)


## Python tree
* Basic tree

<img src = "https://user-images.githubusercontent.com/53554014/102338083-b2c8fe00-3fd6-11eb-9395-1f9dd30d8d82.png" height=50% alt="basic"></img>

코딩 도장에서 진행했던 별 모양 출력이 기억나시나요? 반복문과 조건문을 활용하여 트리를 만들 수 있습니다! 저는 여기에 ANSI escape code를 이용하여 색을 주었어요. 파이썬에서는 `pip install colorama` 하셔서 사용할 수 있습니다.

* tree_random_deco.py

<img src="https://user-images.githubusercontent.com/53554014/102234761-f66b2b80-3f34-11eb-8d30-d4a48dd59d62.png" height=50% alt="python tree with random deco"></img>

그냥 트리를 밋밋하니까 이번에는 데코를 줘 볼게요. 해당 코드는 @AndrewJ7823 님의 JS 코드를 참고하였습니다.

* tree_random_deco_move.py

<img src="https://user-images.githubusercontent.com/53554014/102339659-d4c38000-3fd8-11eb-8cae-84be2505f671.gif" height=50% alt=move tree></img>

최근에 멀티쓰레딩을 배웠던 것이 기억나시나요? 멀티쓰레딩을 이용하여 움직이는 효과를 줘 보았습니다. 참고로 멀티쓰레드 처리하면 속도가 무지무지 빨라서 일부러 쓰레드 하나 처리 후 몇 초간 wait 타임을 걸었습니다!

## How to use Github
여러분의 트리를 자랑해 주세요.
1. Fork : 현재 레포(seraaaayeo/Wish_UR_Merry_Christmas)를 각자 계정으로 포크로 푹 찍어서 떠 간다! Fork 후에는 yourID/Wish_UR_Merry_Christmas, forked from seraaaayeo/Wish_UR_Merry_Christmas 라고 뜰 것입니다.
2. Clone : 개인 계정으로 레포를 포크해갔으면, 이 레포를 Clone하여 로컬 PC로 복사해갑니다. `git clone https://주소.git` 명령어를 이용하여 개인 PC의 원하는 경로로 복사해주세요. 저는 주로 *workspace/Python* 경로에 복사한답니다!
3. 포크떠온 원래 레포 주소(*https://github.com/seraaaayeo/Wish_UR_Merry_Christmas.git*)도 추가로 원격 연결해주세요. Clone을 했기 때문에 origin이라는 이름으로 remote 연결이 자동으로 되어 있을 것입니다. 원래 레포 주소는 다른 이름으로 연결해줄게요. 저는 tree라는 이름으로 연결하였습니다. `git remote add tree https://github.com/seraaaayeo/Wish_UR_Merry_Christmas`
4. 열심히 트리를 만듭시다 =3=3
5. (Recommendation) 코드 작성 후 커밋하기 전 충돌(Conflict) 방지를 위해 변경사항을 받아옵니다. `git fetch tree` or `git pull tree master`
6. 이제 모든 변경사항이 업데이트 되었습니다! 내가 만든 트리를 추가할게요. `git add your_tree.py` -> `git commit -m "Your Message"`
7. 포크떠온 내 계정의 레포에 푸시합니다. `git push origin master`
8. 성공적으로 푸시가 완료되면 *Compare & Pull Request* 버튼이 활성화됩니다. 버튼을 눌러서 충돌이 있는지 확인하고, 충돌이 없으면 *Able to merge*라고 뜰 거에요. 풀리퀘 메시지를 적고 *Create Pull Request* 버튼을 누르면 풀리퀘 끝! 참고로 이 과정에서 코드를 피드백해줄 리뷰어를 지정할 수 있답니다.
9. 이제 풀리퀘를 받은 원래 레포 주인이 코드를 확인할거에요. 코드를 확인하고 merge하기 전인 이 과정에서 코드리뷰가 들어갑니다. 이상이 없을 경우 주인장이 merge해 주면 여러분의 코드가 주인장의 레포에 예쁘게 올라간답니다!
