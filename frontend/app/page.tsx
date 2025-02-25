'use client'

import React, { useState } from 'react'
import axios from 'axios'
import FileUpload from '../components/ui/fileUpload'
import { Loader2 } from 'lucide-react'
import Link from 'next/link'

const Page = () => {
  const [imageUrl, setImageUrl] = useState<string | null>(null)
  const [peopleCount, setPeopleCount] = useState<number | null>(null)
  const [loading, setLoading] = useState<boolean>(false)

  const handleFileUpload = async (file: File) => {
    const formData = new FormData()
    formData.append('file', file)

    setLoading(true)

    try {
      const response = await axios.post('http://localhost:8000/upload', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      })

      const { imageUrl, peopleCount } = response.data
      setImageUrl(imageUrl)
      setPeopleCount(peopleCount)
    } catch (error) {
      console.error('Error uploading file', error)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-8">
      <div className="bg-white shadow-2xl rounded-3xl p-8 w-full max-w-5xl text-center">
        <h1 className="text-3xl font-extrabold mb-6 text-black">Person Detection Upload</h1>

        <div className="w-9/10 max-w-4xl mx-auto">
          <FileUpload onFileUpload={handleFileUpload} />
        </div>

        {loading && (
          <div className="flex justify-center items-center mt-6">
            <Loader2 className="animate-spin w-8 h-8 text-blue-600" />
            <span className="ml-3 text-gray-700 text-lg">Processing...</span>
          </div>
        )}

        {imageUrl && peopleCount !== null && !loading && (
          <div className="mt-8 w-9/10 max-w-5xl mx-auto">
            <h2 className="text-2xl font-semibold text-black">People Count: {peopleCount}</h2>
            <div className="flex justify-center mt-6">
              <img src={imageUrl} alt="Processed Image" className="rounded-lg shadow-lg w-full h-auto" />
            </div>
          </div>
        )}
      </div>

      {/* History Page Popup */}
      <div className="fixed bottom-8 right-8 bg-blue-600 text-white px-6 py-3 rounded-2xl shadow-lg hover:bg-blue-700 transition-all">
        <Link href="/history" target="_blank" rel="noopener noreferrer">
          📜 View Database
        </Link>
      </div>
    </div>
  )
}

export default Page