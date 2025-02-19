import React from 'react'
import { useDropzone } from 'react-dropzone'

type FileUploadProps = {
  onFileUpload: (file: File) => void
}

const FileUpload: React.FC<FileUploadProps> = ({ onFileUpload }) => {
  const { getRootProps, getInputProps } = useDropzone({
    accept: { 'image/*': [] }, // Fixes the TypeScript error for 'accept'
    onDrop: (acceptedFiles) => {
      if (acceptedFiles.length > 0) {
        onFileUpload(acceptedFiles[0])
      }
    }
  })

  return (
    <div
      {...getRootProps({ className: 'dropzone' })}
      className="border-2 border-dashed border-gray-400 p-6 text-center rounded-lg bg-gray-50"
    >
      <input {...getInputProps()} />
      <p className="text-gray-700 font-medium">Drag & drop an image file, or click to select one</p>
    </div>
  )
}

export default FileUpload
