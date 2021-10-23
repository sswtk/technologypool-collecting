/**
 * @Author: roninsswang
 * @Date: 2021/10/23 10:02 下午
 * @File: client
 */

package main

import (
	"fmt"
	"rpc_go_implement/new_helloworld/client_proxy"
)

func main(){
	client := client_proxy.NewHelloServiceClient("tcp", "localhost:1234")
	var reply string
	err := client.Hello("ronin", &reply)
	if err != nil{
		panic("调用失败")
	}
	fmt.Println(reply)
}
