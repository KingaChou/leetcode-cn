// Package main url: https://leetcode-cn.com/problems/intersection-of-two-linked-lists
package main

// ListNode 链表结点结构
type ListNode struct {
	Val  int
	Next *ListNode
}

func main() {

}

// getIntersectionNode 找到两个单链表相交的起始节点
// 思路：不考虑循环链表的情况。两条链表只要从较短链表的位置开始比较即可。
func getIntersectionNode(headA, headB *ListNode) *ListNode {
	if headA == nil || headB == nil {
		return nil
	}

	// 计算两条链表的长度
	aLen, bLen := 1, 1
	for curNode := headA.Next; curNode != nil; curNode = curNode.Next {
		aLen++
	}
	for curNode := headB.Next; curNode != nil; curNode = curNode.Next {
		bLen++
	}

	// 较长的链表先移动N个结点。N为两条链表的长度差值。
	curNodeA := headA
	curNodeB := headB
	minLen := aLen
	if minLen > bLen {
		minLen = bLen

		for i := 0; curNodeA != nil && i < aLen-bLen; curNodeA = curNodeA.Next {
			i++
		}
	} else {
		for i := 0; curNodeB != nil && i < bLen-aLen; curNodeB = curNodeB.Next {
			i++
		}
	}

	// 比较两条链表当前结点的地址是否相同，是则说明相交，返回当前结点。
	for curNodeA != nil && curNodeB != nil {
		if curNodeA == curNodeB {
			return curNodeA
		}

		curNodeA = curNodeA.Next
		curNodeB = curNodeB.Next
	}

	return nil
}
