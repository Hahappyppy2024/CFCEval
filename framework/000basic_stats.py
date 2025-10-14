import os
commont_hint_dir_copilot="D:/000_PHD_project/all_src_for_codeql/generates/5_starcoder2_7b/cleaned_com_hint/" #516/2
recon_rename_dir_starcoder2_com="D:/000_PHD_project/all_src_for_codeql/generates/recons_rename_working/5_Starcoder2_7b/com/recon/reconstructed_com/"
recon_rename_dir_starcoder2_hint="D:/000_PHD_project/all_src_for_codeql/generates/recons_rename_working/5_Starcoder2_7b/hint/rename/rename_hint/"



def count_files(src):
    num_files=[]
    work_after_trans=[]
    for folder in os.listdir(src):
        # print(folder)
        s = os.path.join(src, folder)
        new_dir = s + "/"
        for item in os.listdir(new_dir):
            print(item)
            name_list=item.split("_")
            work_after_trans.append(name_list[0].replace("PY",""))
            num_files.append(item)

    print(len(num_files))
    print(work_after_trans)
    return


count_files(recon_rename_dir_starcoder2_hint)

# notwork=[57,91,100,101,102,103,104,105,112,113,125,142,145,146,
#     147,148,155,161,182,187,192,193,199,201,204,205,207,209,
#     211,212,215,218,219,224,225,232,247,267,268]

