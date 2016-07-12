#! /usr/bin/python2.6
#! coding=utf-8
#! 增加/删除/修改xml

#运行有问题

from xml.etree.ElementTree import ElementTree,Element
from xml.dom.minidom import parse
import xml.dom.minidom


#读取并解析xml文件
def read_xml(in_path):
    tree = ElementTree()
    tree.parse(in_path)
    return tree

#将xml文件写出
def write_xml(tree, out_path):
    tree.write(out_path, encodind="utf-8", xml_declaration=True)

#判断某个节点是否包含所有传入参数属性
def if_match(node, kv_map):
    for key in kv_map:
        if node.get(key) != kv_map.get(key):
            return False
    return True

#---Search---
#查找某个路径匹配的所有节点
def find_nodes(tree, path):
    return tree.findall(path)

#根据属性及属性值定位符合的节点, 返回节点
def get_node_by_keyvalue(nodelist, kv_map):
    result_nodes = []
    for node in nodelist:
        if if_match(node, kv_map):
            result_nodes.append(node)
    return result_nodes

#----change-----
#修改/增加 /删除 节点的属性及属性值
def change_node_properties(nodelist, kv_map, is_delete=False):
    for node in nodelist:
        for key in kv_map:
            if is_delete:
                if key in node.attrib:
                    del node.attrib[key]
            else:
                node.set(key, kv_map.get(key))

#改变/增加/删除一个节点的文本
def change_node_text(nodelist, text, is_add=False, is_delete=False):
    for node in nodelist:
        if is_add:
            node.text += text
        elif is_delete:
            node.text = ""
        else:
            node.text = text
#创造新节点
def create_node(tag, property_map, content):
    element = Element(tag, property_map)
    element.Text = content
    return element


#给一个节点添加子节点
def add_child_node(nodelist, element):
    for node in nodelist:
        node.append(element)

#属性及属性值定位一个节点，并删除之
def del_node_by_tagkeyvalue(nodelist, tag, kv_map):
    for parent_node in nodelist:
        children = parent_node.getchildren()
        for child in children:
            if child.tag == tag and if_match(child, kv_map):
                parent_node.remove(child)


if __name__ == "__main__":

    #1，读取xml文件
    tree = read_xml("check.xml")

    #2, 属性修改
    #找到父节点
    nodes = find_nodes(tree, "processers/processer")


#    print nodes




