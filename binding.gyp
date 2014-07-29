{
  "includes": [ "deps/common-xz.gypi" ],
  "targets": [
    {
      "target_name": "node_xz",
      "dependencies": [
        "deps/xz.gyp:xz"
      ],
      "sources": [
        "src/c++/node_xz.cpp",
        "src/c++/engine.h",
        "src/c++/engine.cpp"
      ],
      "libraries": [
        "<(SHARED_INTERMEDIATE_DIR)/xz-<@(xz_version)/src/liblzma/.libs/liblzma.a"
      ]
    }
  ]
}
