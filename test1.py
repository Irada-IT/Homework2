import subprocess
def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False
folder_in = "/home/user/tst"
folder_out = "/home/user/out"
folder_ext = "/home/user/folder1"
folder_ext2 = "/home/user/folder2"
def test_step1():
    #test1
    assert checkout("cd /home/user/tst; 7z a ../out/arx2", "Everything is Ok"), "test1 FAIL"
def test_step2():
    #test2
    assert checkout("cd /home/user/out; 7z e arx2.7z -o/home/user/folder1 -y", "Everything is Ok"), "test2 FAIL"
def test_step3():
    #test3
    assert checkout("cd /home/user/out; 7z t arx2.7z", "Everything is Ok"), "test3 FAIL"
def test_step4():
    #test4
    assert checkout("cd {}; 7z u arx2.7z".format(folder_in),"Everything is Ok"), "test4 FAIL"
def test_step5():
    #test5
    assert checkout("cd {}; 7z d arx2.7z".format(folder_out), "Everything is Ok"), "test5 FAIL"
def test_step6():
    #test6
    res1 = checkout("cd {}; 7z a {}/arx2".format(folder_in, folder_out), "Everything is Ok")
    res2 = checkout("ls {}".format(folder_out), "arx2.7z")
    assert res1 and res2, "test6 FAIL"
def test_step7():
    # test7
    res1 = checkout("cd {}; 7z e arx2.7z -o{} -y".format(folder_out, folder_ext), "Everything is Ok")
    res2 = checkout("ls {}".format(folder_ext), "test1")
    res3 = checkout("ls {}".format(folder_ext), "test2")
    assert res1 and res2 and res3, "test7 FAIL"
def test_step8():
    # test8
    res1 = checkout("cd {}; 7z l arx2.7z".format(folder_out, folder_ext), "file1.txt")
    res2 = checkout("cd {}; 7z l arx2.7z".format(folder_out, folder_ext), "file2.txt")
    assert res1 and res2, "test8 FAIL"
def test_step9():
    # test9
    res1 = checkout("cd {}; 7z x arx2.7z -o{} -y".format(folder_out, folder_ext2), "Everything is Ok")
    res2 = checkout("ls {}".format(folder_ext2), "test1")
    res3 = checkout("ls {}".format(folder_ext2), "test2")
    res4 = checkout("ls {}".format(folder_ext2), "test3")
    res5 = checkout("ls {}".format(folder_ext2), "test4")
    assert res1 and res2 and res3 and res4 and res5, "test9 FAIL"