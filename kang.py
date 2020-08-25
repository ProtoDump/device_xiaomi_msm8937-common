import os
import shutil

KANG_VENDOR="../../../device/caf/"
VENDOR="../../../vendor/xiaomi/msm8937-common/proprietary/"

VENDOR_LIST="""vendor/lib/hw/keystore.msm8937.so
vendor/lib/libkeymasterutils.so
vendor/lib/libkeymasterprovision.so
vendor/lib/libkeymasterdeviceutils.so
vendor/lib64/hw/keystore.msm8937.so
vendor/lib64/libkeymasterutils.so
vendor/lib64/libkeymasterprovision.so
vendor/lib64/libkeymasterdeviceutils.so
vendor/lib/hw/sound_trigger.primary.msm8937.so
vendor/lib/libadpcmdec.so
vendor/lib/libsmwrapper.so
vendor/lib64/hw/sound_trigger.primary.msm8937.so
vendor/lib/libUBWC.so
vendor/lib/libfastcrc.so
vendor/lib/libstreamparser.so
vendor/lib/libvideoutils.so
vendor/lib/libvqzip.so
vendor/lib64/libUBWC.so
vendor/lib64/libfastcrc.so
vendor/lib64/libstreamparser.so
vendor/lib64/libvideoutils.so
vendor/bin/pm-proxy
vendor/bin/pm-service
vendor/lib/libperipheral_client.so
vendor/lib64/libperipheral_client.so
vendor/bin/thermal-engine
vendor/lib/libthermalclient.so
vendor/lib64/libthermalclient.so
"""



SPLIT_VENDOR_LIST = VENDOR_LIST.split("\n")

for file in SPLIT_VENDOR_LIST:
	if file[0] != "v":
		shutil.copy2(f"{KANG_VENDOR}system/{file}", f"{VENDOR}{file}")
	else:
		shutil.copy2(f"{KANG_VENDOR}{file}", f"{VENDOR}{file}")
	print(f"Copied file from {KANG_VENDOR}{file} to {VENDOR}{file}")

