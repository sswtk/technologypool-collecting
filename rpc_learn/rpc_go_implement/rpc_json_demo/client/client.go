/**
 * @Author: roninsswang
 * @Date: 2021/10/17 4:32 下午
 * @File: client
 */

package main

import (
	"fmt"
	"net"
	"net/rpc"
	"net/rpc/jsonrpc"
)

func main() {
	conn, err := net.Dial("tcp", "localhost:1234")
	if err != nil {
		panic("Connect failed")
	}
	var reply string
	client := rpc.NewClientWithCodec(jsonrpc.NewClientCodec(conn))
	err = client.Call("HelloService.Hello", "sswang", &reply)
	if err != nil{
		panic("Called Error")
	}
	fmt.Println(reply)
}
