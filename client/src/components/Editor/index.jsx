import React from "react";
import { EditorState } from "draft-js";
import { Editor } from "react-draft-wysiwyg";
import { convertToHTML } from "draft-convert";
import "react-draft-wysiwyg/dist/react-draft-wysiwyg.css";
import { useState } from "react";
import "./style.css";
import { useEffect } from "react";
import DOMPurify from "dompurify";

function createMarkup(html) {
  return {
    __html: DOMPurify.sanitize(html),
  };
}
const CustomEditor = () => {
  const [editorState, setEditorState] = useState(() =>
    EditorState.createEmpty()
  );
  const [convertedContent, setConvertedContent] = useState(null);

  useEffect(() => {
    let html = convertToHTML(editorState.getCurrentContent());

    setConvertedContent(html);
  }, [editorState]);
  return (
    <>
      <div style={{ width: "100%" }}>
        <Editor
          editorState={editorState}
          onEditorStateChange={setEditorState}
          wrapperClassName="wrapper-class"
          editorClassName="editor-class"
          toolbarClassName="toolbar-class"
          toolbar={{
            options: ["inline", "blockType", "fontFamily"],
            fontFamily: {
              options: [
                "Arial",
                "Georgia",
                "Impact",
                "Tahoma",
                "Times New Roman",
                "Verdana",
              ],
            },
          }}
        />
      </div>
      <div>
        <div
          className="preview"
          dangerouslySetInnerHTML={createMarkup(convertedContent)}
        ></div>
      </div>
    </>
  );
};

export default CustomEditor;
