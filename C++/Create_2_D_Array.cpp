#include <vector>

//使用二维指针创建二维数组
int **Create_2_D_Array(int row, int col)
{
	int **arr = NULL;
	arr = new int*[row];
	for (int i = 0; i < row; i++)
		arr[i] = new int[col];
	return arr;
}

//释放二维指针创建的二维数组
void Delete_2_D_Array(int **arr, int row, int col)
{
	for (int i = 0; i < row; i++)
	{
		delete[] arr[i];
		arr[i] = NULL;
	}

	/*
	//需要在外层再次释放
	delete[] arr;
	arr = NULL;
	*/
	
}

//使用vector创建二维数组
vector<vector<int>> Create_2_D_Vector(int row, int col)
{
	//法1
	vector<vector<int> > arr(row, vector<int>(col));
	
	//法2
	/*
	vector<vector<int> > arr;
	arr.resize(row);
	for (int i = 0; i < row; i++)
		arr[i].resize(col);
	*/
	return arr;
}


