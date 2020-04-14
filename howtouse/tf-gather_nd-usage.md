

## tf.gather_nd() 사용법



### Usage 1

> output = gather_nd(param, indices)  
> where param.shape=(4, 12, 5), indices.shape=(3, 2)  

`indices`에서 가장 안쪽의 차원, 즉 2에 해당하는 두 번째 차원에 param에서 추출해야할 인덱스 데이터가 들어있다.  

그 위의 차원은 몇 개의 데이터를 몇 겹으로 뽑아낼 것이냐를 결정하는 것이다.  

`param`의 두 가지 인덱스를 (i, k)라고 하면 현재의 `indices.shape=(3,2)` 이므로

`gather_nd(param, indices)`를 실행하면 `param[i, k]`를 세 번 인덱싱한 결과를 모아서 보여준다.  아래는 구현 원리를 보여주는 예시다.

```python
# shape=(3, 2)
indices = tf.Tensor([[0, 1], [2, 9], [3, 7]])
# output = [param[0, 1], param[2, 9], param[3, 7]]
output = gather_nd(param, indices)
```

이때 `param[i, k]` 자체가 5차원이므로 이들을 묶으면 `output.shape=(3, 5)`가 된다.



### Usage 2

> output = gather_nd(param, indices)  
> where param.shape=(4, 12, 5), indices.shape=(3, 6, 2)  

이번에는 `indices`의 차원이 하나 늘어났는데 작동방식은 Usage 1과 같다. 차이점은 Usage 1에서는 인덱싱을  세 번만해서 모았는데 이번에는 인덱스 쌍이 (3, 6)개, 즉 18개가 있으므로 18번 인덱싱한 결과를 (3, 6)형태의 두 개의 차원에 구조적으로 배치한다. 아래는 구현 원리를 보여주는 예시다.

```python
# shape=(3, 6, 2)
indices = tf.Tensor([ [[0, 1], [2, 9], [3, 7], [0, 1], [2, 9], [3, 7]], 
                       [...], 
                       [...] ]) 	
# output = [ [param[0,1], param[2,9], param[3,7], param[0,1], param[2,9], param[3,7]], 
#            [...], 
#            [...] ]
output = gather_nd(param, indices)
```

각각의 인덱싱 결과는 5차원이므로 `output.shape=(3, 6, 5)`가 된다.



### Usage 3

> output = gather_nd(param, indices, batch_dims=1)  
> where param.shape=(4, 12, 5), indices.shape=(4, 3, 2)  

이번에는 `batch_dims`라는 입력인자가 들어간다. Usage 1, 2에서는 출력의 shape이 `param`보다는 `indices`에 의해 결정이 됐다. 하지만 batch로 결과를 만들때는 모든 batch index에 대해 동일한 연산을 해야 하므로 `param`의 batch 차원과 `indices`의 첫 번째 차원의 크기가 같아야 한다. (위에서는 4로 맞춤)   

batch 내부의 각 데이터에 대해서 똑같은 수의 인덱싱을 한다면 (위에서는 데이터마다 3번씩 인덱싱) 굳이 `indices`에 batch index를 입력하지 않아도 현재 인덱스가 몇 번째 배치 데이터에 대한 인덱스인지 알 수 있다. 그래서 batch 처리를 하는 경우에는 **batch index를 생략하고 `batch_dims=1`을 입력**하면 된다.  아래는 구현 원리는 보여주는 예시다.

```python
# shape=(4, 3, 2)
indices = tf.Tensor([ [[1], [4], [5]], # batch index=0 에 대해 1, 4, 5 row 추출
                      [[3], [2], [1]], # batch index=1 에 대해 3, 2, 1 row 추출
                      [...], 
                      [...] ]) 	
# output = [ [param[0, 1], param[0, 4], param[0, 5]], 
#            [param[1, 3], param[1, 2], param[1, 1]], 
#            [...], 
#            [...] ]
output = gather_nd(param, indices)
```

각각의 인덱싱 결과는 5차원이므로 `output.shape=(4, 3, 5)`가 된다.

