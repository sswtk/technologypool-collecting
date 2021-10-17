/**
 * @Author: roninsswang
 * @Date: 2021/10/17 10:44 上午
 * @File: client
 */

package main

import (
	"fmt"
	"net/rpc"
)

func main(){
	//建立连接
	client, err := rpc.Dial("tcp", "localhost:1234")
	if err != nil{
		panic("Connect Error")
	}
	//var reply *string = new(string)
	var reply string  //string有默认值
	err = client.Call("HelloService.Hello", "sswang", &reply)
	if err != nil {
		panic("Called Error")
	}
	fmt.Println(reply)
}
