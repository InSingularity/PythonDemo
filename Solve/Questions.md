##                                   写代码时遇到的问题

1. 最好不要交叉引用文件，除非使用了预编译来防止重复引用（[解答](https://blog.csdn.net/hazir/article/details/38600419?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-6.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-6.control)）

2. 尽量在.cpp中包含头文件，可以预防重复定义（[解答](https://blog.csdn.net/xueruifan/article/details/50569639)）

3. free后赋值NULL,避免野指针

4. 

   ```c++
   n = -2147483648;
   //error C4146: 一元负运算符应用于无符号类型，结果仍为无符号类型
   ```

   虽然明明 int 最小值是 -2147483648，但我们就是无法用int n = -2147483648;表示。

   需要用 -2147483647-1来表示（[解答](https://blog.csdn.net/liuhhaiffeng/article/details/53991071)）
   
5. 无法 从“const char [19]”转换为“char *”

   ```c
   void error_handling(char * message)
   {
   	fputs(message, stderr); //想错误流输入
   	fputc('\n', stderr);
   	exit(1);
   }
   
   int main(int argc, char * argv[])
   {
   	error_handling("WSAStartup() error");
   }
   
   //上诉代码出现的问题如下：
   //“void error_handling(char *)”: 无法将参数 1 从“const char [19]”转换为“char *”
   //解决方法：error_handling的参数改成cosnt,如下：
   //void error_handling(cosnt char * message)
   ```

 ## vs中遇到的问题 

1. vs中有多个项目，可设置启动项目来切换。
2. main中的参数表示（设置位置：菜单[项目] -> 属性页 -> 配置属性 -> 调试->命令参数）
   - argc ：表示argv中的参数个数（至少位1，无需设置，自动识别）
   - argv：存储命令参数，用空格分隔多个参数（argv[0]始终保存着执行文件的位置）
3. 设置了参数但是在代码中未识别，需要检查配置（Debug/Release）和平台（x64/x86）

## Github遇到的问题

1. Q:Github的.md文件图片无法显示

   A:查看源代码中的斜杠，需要为“/”。因为window上"\\"也可以,所以需要加以区分。

